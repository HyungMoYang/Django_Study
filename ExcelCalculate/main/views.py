from django.shortcuts import render, redirect
from .models import * # DB model 추가
from random import * # for 난수 처리
from sendEmail.views import * # sendEmail app의 views.py의 모든것 import

# Create your views here.
# 메인 화면 - index
def index(request):
    return render(request, 'main/index.html')

# 회원가입 처리
def signup(request):
    return render(request, 'main/signup.html')

def join(request): # 인증코드 입력 화면
    # print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save() # html file에서 위의 정보를 받아와서 DB에 저장

    # 4자리 인증 코드를 위한 난수 처리
    code = randint(1000, 9999)
    response = redirect('main_verifyCode') # redirect를 위한 페이지를 리턴하지 않고 저장, 쿠기 저장을 위함. 
    response.set_cookie('code', code) # 해당 페이지 쿠키를 세팅한다. 
    response.set_cookie('user_id', user.id)
    
    # 이메일 발송 함수 호출
    send_result = send(email, code) # sendEmail의 함수 호출
    if send_result: 
        return response
    else:
        return HttpResponse("이메일 발송에 실패했습니다.")

# 로그인 처리
def signin(request):
    return render(request, 'main/signin.html')

# 유효 코드인증
def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    user_code = request.POST['verifyCode'] # 해당 url의 request에서 user가 입력한 코드 값을 받아옴. 
    cookie_code = request.COOKIES.get('code') # 저장된 쿠기에서 코드 값을 가져옴 -> 현재 26줄에 있는 코드 

    # 코드 유효 검사 
    if user_code == cookie_code:
        user = User.objects.get(id = request.COOKIES.get('user_id')) # DB에서 쿠키에 저장된 user_id 값과 같은 값을 불러온다. 
        user.user_validate = 1 # 아이디 유효하게 변경
        user.save() # DB에 새로 저장
        response = redirect('main_index') # 페이지 저장 
        response.delete_cookie('code') # 기존 쿠키 삭제
        response.delete_cookie('user_id')
        response.set_cookie('user', user) # 새 쿠키 저장
        return response
    else:
        redirect('main_verifyCode')


def result(request):
    return render(request, 'main/result.html')



