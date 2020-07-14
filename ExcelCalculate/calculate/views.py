from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def calculate(request):
    file = request.FILES['fileInput']
    # print(f"# 사용자가 등록한 파일의 이름: {file}")
    df = pd.read_excel(file, sheet_name='Sheet1', header = 0)
    
    # grade별 value 리스트 만들기
    grade_dic = {} # create dict
    total_row_num = len(df.index)
    for i in range(total_row_num):
        data = df.loc[i] # df의 i-1행의 데이터 
        if not data['grade'] in grade_dic.keys():
            grade_dic[data['grade']] = [data['value']]
        else:
            grade_dic[data['grade']].append(data['value'])
    
    # grade별 최솟값 최댓값 평균값 구하기
    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {} # 'grade_calculate_dic'의 key 값의 value로 다시 dict
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key])) / len(grade_dic[key])

    # 결과 출력
    grade_list = list(grade_calculate_dic.keys())
    grade_list.sort()
    for key in grade_list:
        print("# grade:", key)
        print("min:", grade_calculate_dic[key]['min'], end='')
        print(" / max:", grade_calculate_dic[key]['max'], end='')
        print(" / avg:", grade_calculate_dic[key]['avg'], end='\n\n')
    
    # 이메일 주소 도메인별 인원 구하기
    email_domain_dic = {}
    for i in range(total_row_num):
        data = df.loc[i] # df의 i-1행의 데이터 
        email_domain = (data['email'].split("@"))[1] # 불러온 행의 'email'열에서 '@'을 구분자로 나눈다. 
        if  email_domain not in email_domain_dic.keys():
            email_domain_dic[email_domain] = 1
        else:
            email_domain_dic[email_domain] += 1
    print("## EMAIL 도메인별 사용 인원")
    for key in email_domain_dic.keys():
        print("#", key, ": ", email_domain_dic[key], "명")

    # return HttpResponse("calculate, calculate function!")
    
    # django에서의 호환을 위해서 데이터를 가공한다.
    grade_calculate_dic_to_session = {}
    for key in grade_list:
        grade_calculate_dic_to_session[int(key)] = {}
        grade_calculate_dic_to_session[int(key)]['max'] = float(grade_calculate_dic[key]['max'])
        grade_calculate_dic_to_session[int(key)]['avg'] = float(grade_calculate_dic[key]['avg'])
        grade_calculate_dic_to_session[int(key)]['min'] = float(grade_calculate_dic[key]['min'])
    request.session['grade_calculate_dic'] = grade_calculate_dic_to_session
    
    request.session['email_domain_dic'] = email_domain_dic
    return redirect('/result')
        
