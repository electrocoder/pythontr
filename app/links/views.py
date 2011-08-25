# -*- coding: utf-8 -*-

from django.shortcuts import render

from pythontr.app.links.models import Link


def index(request):
    """
    Veritabanında kayıtlı olan linkleri listelemek için kullanılır.
    """
    
    
    links = Link.objects.all()
    
    response_dict = {
        'links': links,
        }

    return render(request, 'links/index.html', response_dict)
