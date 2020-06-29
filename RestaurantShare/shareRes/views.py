from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

# index
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants': restaurants}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content) # request를 받아서 'templates/shareRes/index.html' render

# detail page
def restaurantDetail(request, res_id): # url을 통해서 오는 값이 GET이 아니라면 request에 담기지 않기 때문에 따로 매개변수로 받아주어야 서버처리가 가능하다.
    restaurant = Restaurant.objects.get(id = res_id) # DB에서 res_id와 같은 값을 가져와서 
    content = {'restaurant': restaurant} # dict를 생성하고 
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurant_detail.html', content) # html file rendering할때 포함해준다. 

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories': categories, 'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']

    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()

    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))

# create page
def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

# category page
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


