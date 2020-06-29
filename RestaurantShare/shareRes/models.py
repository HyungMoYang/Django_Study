from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) # Category 모델 참조, on_delete-참조 모델 삭제시 행동 -> default 값으로 설정 한다. 
    restaurant_name = models.CharField(max_length = 100)
    restaurant_link = models.CharField(max_length = 500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length = 50)
