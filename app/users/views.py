# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from pythontr.app.users.forms import Signup

def profile(request, username):
    """ Üye profilini göstermek için kullanılıyor. """
    
    user = get_object_or_404(User, username = username)
       
    return render(request, 'users/profile.html', locals())


def signup(request):
    """ Üye kayıt için kullanılıyor. """
    
    if request.method == "POST":
        form = Signup(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            return redirect(reverse('blog:index_path'))
    else:
        form = Signup()
        
    return render(request, 'users/signup.html', locals())
            
