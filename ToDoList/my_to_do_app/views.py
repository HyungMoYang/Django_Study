# my_to_do_app > views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'my_to_do_app/index.html', content) # 보여주고 싶은 html file을 rendering한다 

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create Todo를 할 거야! =>" + user_input_str)