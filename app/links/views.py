# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse


from pythontr.app.links.models import Link


def index(request, page=1):
    """
    Veritabanında kayıtlı olan linkleri listelemek için kullanılır.
    
    Her sayfada 20 link vardır.
    """
    
    links = Link.objects.filter(accepted = True)
    
    links = Paginator(links, 20)
    
    try:
        # /links/page/2/ ile girilmişse onu getir.
        page = links.page(page)
    except EmptyPage:
        # getiremezsen ilk sayfaya yönlendir.
        return redirect(reverse('links:index_path_page', args=[1]))
            
    links = page.object_list

    return render(request, 'links/index.html', locals())
