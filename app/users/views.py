# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.contrib.auth.models import User

from pythontr.app.users.forms import Signup
from pythontr.app.users.models import Profile

def profile(request, username):
    """ Üye profilini göstermek için kullanılıyor. """
    
    user = get_object_or_404(User, username = username)
       
    return render(request, 'users/profile.html', locals())


def signup(request):
    """ Üye kayıt için kullanılıyor. """

    if request.method == "POST":
        form = Signup(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save()
            profile = Profile(
                web = form.cleaned_data['web'],
                bio = form.cleaned_data['bio'],
                photo = form.cleaned_data['photo'],
                user = user,
                )
            profile.save()
            
            messages.success(request, 'Üye kaydı başarılı. Aramıza hoşgeldin!')

            return redirect(reverse('blog:index_path'))
    else:
        form = Signup()
        
    return render(request, 'users/signup.html', locals())
            
