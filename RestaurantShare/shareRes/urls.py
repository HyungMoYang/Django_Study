# shareRes > urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # index
    path('', views.index, name = 'index'),
    # detail page
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'), # <>는 동적인 값을 표현한다. 
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
    # create page
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'),
    # category page
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'),
]
