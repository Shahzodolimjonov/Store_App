# import re
# from django.core.exceptions import ValidationError
# from django import forms
# from .models import *
#
#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control'
#             })
#         }
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if re.match(r'\d', title):
#             raise ValidationError('error')
#         return title




from django import forms
from django.core.exceptions import ValidationError

from .models import Category, News
import re

class SearchForm(forms.Form):
    title = forms.CharField(label='search',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

class NewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('error')
        return title
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content)<6:
            raise ValidationError('error')
        return content

class Boss(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('error')
        return title


class Search(forms.ModelForm):
    class Meta:
        fields = ['title']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

