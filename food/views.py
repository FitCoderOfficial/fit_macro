from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FoodForm
from .models import Food
from members.models import Member

# Create your views here.

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'
    context_object_name = 'foods'

class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('food-list')

class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('food-list')

class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('food-list')

@method_decorator(login_required, name='dispatch')
class FoodAddToLogView(CreateView):
    model = Member
    fields = ['food', 'serving_size', 'meal']
    template_name = 'add_food_to_log.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        member = Member.objects.get(user=self.request.user)
        form.instance.member = member
        return super().form_valid(form)

@login_required
def food_search(request):
    if request.method == 'POST':
        search_str = request.POST['search']
        if search_str:
            foods = Food.objects.filter(food_name__icontains=search_str, db_category__icontains='branded')
            return render(request, 'food_search.html', {'foods': foods, 'search': search_str})
        else:
            return redirect('food-search')
    else:
        return render(request, 'food_search.html', {})
