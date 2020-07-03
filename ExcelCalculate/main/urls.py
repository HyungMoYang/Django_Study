from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'), # 메인 화면
    path('signup', views.signup, name='main_signup'), # 로그인
    path('signin', views.signin, name='main_signin'), # 회원 가입
    path('verifyCode', views.verifyCode, name='main_verifyCode'), # 인증코드 입력 화면
    path('verify', views.verify, name='main_verify'), # 인증 코드 확인 기능 
    path('result', views.result, name='main_result'), # 결과 화면
]