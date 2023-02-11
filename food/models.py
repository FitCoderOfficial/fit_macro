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
       

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    year_of_manufacture = models.PositiveIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    main_category = models.CharField(max_length=100)
    detailed_classification = models.CharField(max_length=100)
    serving_size = models.PositiveIntegerField()
    serving_unit = models.CharField(choices=UNIT_CHOICES, max_length=2)
    total_contents = models.PositiveIntegerField(blank=True, null=True)
    total_calories = models.FloatField(blank=True, null=True)
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
    

class FoodLog(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    serving_size = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)