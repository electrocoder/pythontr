# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse


from pythontr.app.links.models import Link


def index(request, page=1):
    """
    Veritabanında kayıtlı olan linkleri listelemek için kullanılır.
    
    Her sayfada 20 link vardır.
    """
    
    
    paginated_links = Paginator(Link.objects.all(), 20)
    
    try:
        # /links/page/2/ ile girilmişse onu getir.
        target_page = paginated_links.page(page)
    except EmptyPage:
        # getiremezsen anasayfaya yönlendir.
        return redirect(reverse('links_path'))
    except:
        # en son çare page değişkenini 1 kabul et.
        target_page = paginated_links.page(1)
        
    
    response_dict = {
        'links': paginated_links.object_list,
        'page': paginated_links,
        }

    return render(request, 'links/index.html', response_dict)
