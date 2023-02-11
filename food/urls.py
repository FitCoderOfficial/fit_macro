from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'food'

urlpatterns = [
    path('', FoodListView.as_view(), name='food-list'),
    path('create/', login_required(FoodCreateView.as_view()), name='food-create'),
    path('<int:pk>/update/', login_required(FoodUpdateView.as_view()), name='food-update'),
    path('<int:pk>/delete/', login_required(FoodDeleteView.as_view()), name='food-delete'),
    path('add-food-to-log/<int:pk>/', login_required(add_food_to_log), name='add-food-to-log'),
]