# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from pythontr.app.documents.models import Document


def index(request):
    documents = Document.objects.all()
    
    response_dict = {
        'documents': documents,
    }
    
    return render(request, 'documents/index.html', response_dict)
    
    
def show(request, pk):
    document = get_object_or_404(Document, pk = pk)
    
    response_dict = {
        'document': document,
    }
    
    return render(request, 'documents/show.html', response_dict)
