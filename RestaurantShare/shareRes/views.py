from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html') # request를 받아서 'templates/shareRes/index.html' render

def restaurantDetail(request):
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurant_detail.html')

def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')
    

def categoryCreate(request):
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')