
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

def food_list(request):
    context = {
        'foods': Food.objects.all()
    }
    return render(request, 'food_list.html', context)



@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Food)
    order_item, created = FoodItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Log_Food.objects.filter(user=request.user, logged=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(logged=False).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Log_Food.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


@login_required
def remove_from_cart(request):
    item = get_object_or_404(Food)
    order_qs = Log_Food.objects.filter(
        user=request.user,
        logged=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(logged=False).exists():
            order_item = FoodItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product")


@login_required
def remove_single_item_from_cart(request):
    item = get_object_or_404(Food)
    order_qs = Log_Food.objects.filter(
        user=request.user,
        logged=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(logged=False).exists():
            order_item = FoodItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product")