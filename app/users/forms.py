# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm

class Signup(UserCreationForm):
    web = forms.URLField(initial = 'http://',
                         label = 'Web adresi',
                         required = False,
        )
    
    bio = forms.CharField(
        widget=forms.Textarea,
        label = "Hakkınızda",
                          )
    
    photo = forms.ImageField(
        label = "Görsel",     
        required = False,
        )        
