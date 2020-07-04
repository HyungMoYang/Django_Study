from django.db import models

# Create your models here.
# 회원 정보를 저장하기 위한 DB 모델
class User(models.Model):
    user_name = models.CharField(max_length = 20) # User ID
    user_email = models.EmailField(unique = True) # User Email , unique 설정
    user_password = models.CharField(max_length = 100) # User password
    user_validate = models.BooleanField(default = False) # Email verify T/F

