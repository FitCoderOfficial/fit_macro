from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.food_list, name='food-list'),
    path('log/', views.log_food, name='log_food'),
]