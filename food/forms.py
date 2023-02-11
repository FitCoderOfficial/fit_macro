from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    serving_size = forms.IntegerField(min_value=1)
    
    class Meta:
        model = Food
        fields = ['category', 'name', 'main_category', 'detailed_classification', 'serving_unit']
        widgets = {
            'serving_unit': forms.RadioSelect(choices=[('g', 'g'), ('ml', 'ml')])
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')
        self.fields['name'].queryset = Food.objects.none()
        
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['name'].queryset = Food.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['name'].queryset = self.instance.category.food_set.order_by('name')
    
    def clean(self):
        cleaned_data = super().clean()
        serving_size = cleaned_data.get('serving_size')
        if serving_size and serving_size < 1:
            raise forms.ValidationError("Serving size must be a positive integer.")
        return cleaned_data