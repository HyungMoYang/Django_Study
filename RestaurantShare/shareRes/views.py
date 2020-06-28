from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content) # request를 받아서 'templates/shareRes/index.html' render

def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurant_detail.html')

def restaurantCreate(request):
    categories = Category.object.all()
    content = {'categories':categories}
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html', content)
    

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName'] # html file에서 input의 적힌 내용을 가져옴 
    new_category = Category(category_name = category_name) # Model class를 사용해서 인스턴스 생성 
    new_category.save() # DB에 저장
    return HttpResponseRedirect(reverse('index')) # redirect index page
    # return HttpResponse("여기가 category Create 기능을 구현할 페이지야!")

def Delete_category(request):
    category_id = request.POST['categoryId'] # POST form에서 name=categoryId인 값(value)를 가져온다.
    delete_category = Category.objects.get(id = category_id) # 위 value랑 같은 인스턴스를 찾아서 가져옴
    delete_category.delete() # DB에서 삭제
    return HttpResponseRedirect(reverse('cateCreatePage')) # 페이지로 리턴 