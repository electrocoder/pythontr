# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.forms import UserCreationForm

class Signup(UserCreationForm):
    web = forms.URLField( initial = 'http://')
    
    bio = forms.CharField(
        widget=forms.Textarea,
        initial = "Kendiniz hakkında birşeyler yazın"
                          )
