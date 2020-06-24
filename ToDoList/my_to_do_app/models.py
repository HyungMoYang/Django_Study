from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 255)
    isDone = models.BooleanField(default=False) # db내에서 완료한 todo를 삭제시키는 것 이 아니라 true/false로 구분한다. 
    
