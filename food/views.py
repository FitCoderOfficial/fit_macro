
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food/food_list.html', {'foods': foods})


@login_required
def log_food(request):
    food_id = request.POST.get('foods')
    if food_id:
        food = Food.objects.get(id=food_id)
        FoodLog.objects.create(
            user=request.user,
            food=food,
            serving_size=food.serving_size,
        )
    return redirect('food:food-list')