from django.shortcuts import render, redirect
from .models import * # DB model 추가

# Create your views here.
# 메인 화면 - index
def index(request):
    return render(request, 'main/index.html')

# 회원가입 처리
def signup(request):
    return render(request, 'main/signup.html')

def join(request): # 인증코드 입력 화면
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()
    return redirect('main_verifyCode')

# 로그인 처리
def signin(request):
    return render(request, 'main/signin.html')

# 유효 코드인증
def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'main/result.html')



