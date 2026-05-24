from django import forms
from .models import Product
from .models import Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'image',
            'price',
            'stock',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = ['rating', 'comment']

        widgets = {
            'rating': forms.Select(
                choices=[
                    (1, '⭐ 1 Star'),
                    (2, '⭐⭐ 2 Stars'),
                    (3, '⭐⭐⭐ 3 Stars'),
                    (4, '⭐⭐⭐⭐ 4 Stars'),
                    (5, '⭐⭐⭐⭐⭐ 5 Stars'),
                ],

                attrs={
                    'class': 'form-control'
                }
            ),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review...'
            })
        }