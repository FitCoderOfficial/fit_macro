from django.db import models
from members.models import Member

UNIT_CHOICES = [
        ('g', 'g'),
        ('ml', 'ml'),
    ]


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
       
    image = models.ImageField(upload_to='food_images', default='default_food.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    year_of_manufacture = models.PositiveIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    main_category = models.CharField(max_length=100)
    detailed_classification = models.CharField(max_length=100)
    serving_size = models.PositiveIntegerField()
    serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=2)
    contents = models.PositiveIntegerField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbohydrates = models.FloatField(blank=True, null=True)
    total_sugars = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    saturated_fatty_acids = models.FloatField(blank=True, null=True)
    trans_fatty_acids = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class FoodItem(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_calories(self):
        return self.quantity * self.item.calories


class Log_Food(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    start_date = models.DateTimeField(auto_now_add=True)
    logged_date = models.DateTimeField()
    logged = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.name

    def get_total(self):
        total = 0
        for logged_food in self.items.all():
            total += logged_food.get_total_calories()
        return total