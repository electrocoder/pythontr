# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage


from pythontr.app.documents.models import Document


def index(request, page=0):
    """
    Belgeleri listeler.
    Her sayfada 20 belge vardır.
    """
    
    paginated_documents = Paginator(Document.objects.all(), 20)
    
    try:
        # /documents/page/2 şeklinde ulaşmayı dene.
        target_page = paginated_posts.page(page)
    except EmptyPage:
        # getiremezsen belgeler anasayfayasına yönlendir.
        return redirect(reverse('documents_index_path'))
    except:
        # en son çare page değişkenini 1 kabul et.
        target_page = paginated_documents.page(1)
        
    
    response_dict = {
        'documents': paginated_documents.object_list,
        'page': paginated_documents,
    }
    
    return render(request, 'documents/index.html', response_dict)
    
    
def show(request, pk):
    """ Belge göstermek için kullanılıyor. """
    
    
    document = get_object_or_404(Document, pk = pk)
    
    response_dict = {
        'document': document,
    }
    
    return render(request, 'documents/show.html', response_dict)
