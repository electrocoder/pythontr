# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request, username):
    """ Editörün profilini göstermek için kullanılıyor. """
    
    user = get_object_or_404(User, username = username)
    
    response_dict = {
        'user': user,
    }
    
    return render(request, 'editors/profile.html', response_dict)
