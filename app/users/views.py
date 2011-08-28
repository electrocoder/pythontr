# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.contrib.auth.models import User, Group

from pythontr.app.users.forms import SignupForm
from pythontr.app.users.models import Profile

from django.forms.formsets import formset_factory

def profile(request, username):
    """ Üye profilini göstermek için kullanılıyor. """
    
    user = get_object_or_404(User, username = username)
       
    return render(request, 'users/profile.html', locals())


def signup(request):
    """ Üye kayıt için kullanılıyor. """

    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        
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
        form = SignupForm()
        
    return render(request, 'users/signup.html', locals())
            

def editors(request):
    """
    Editörleri listeliyor.
    """
    
    group = Group.objects.get(pk = 1)
    editors = group.user_set.all()
    
    return render(request, 'users/show_editors.html', locals())
    
    
