from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['fullName', 'email', 'message','phoneNumber']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'location', 'client','timeframe','Commodities','body','image']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'location': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'client': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'timeframe': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'Commodities': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'image': forms.ClearableFileInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
            }),
            'body': forms.Textarea(),
        }

class ProjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImages
        fields = ['image']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','image']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'image': forms.ClearableFileInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
            }),
            'body': forms.Textarea(),
        }

class GoldPriceForm(forms.ModelForm):
    class Meta:
        model = GoldPrice
        fields = ['usd', 'usdtoz',]
        widgets = {
            'usd': forms.NumberInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter USD value here'
            }),
            'usdtoz': forms.NumberInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter USD to OZ value here'
            }),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title','body','image']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'image': forms.ClearableFileInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
            }),
            'body': forms.Textarea(),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'role', 'email','profile','image']
        widgets = {
            'name': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'role': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            'email': forms.TextInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
                'placeholder': 'Enter title here'
            }),
            
            'image': forms.ClearableFileInput(attrs={
                'style': 'font-size: 16px; color: #333; border: 2px solid grey; padding: 7px; border-radius: 5px; width: 100%; margin-bottom: 20px;',
            }),
            'profile': forms.Textarea(),
        }


class ProjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImages
        fields = ['image']

class ServicePointForm(forms.ModelForm):
    class Meta:
        model = ServicePoint
        fields = ['point']