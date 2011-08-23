# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page
from django.http import Http404

from pythontr.app.posts.models import Post, Topic

#@cache_page(30)
def index(request, page=1):
    """
    Anasayfa.
    '/' adresini kullanır.
    Her sayfada 20 gönderi vardır.
    Varsayılan olarak ilk sayfayı gösterir.
    
    30 saniye kaşelenir.
    """
    
    posts = Post.objects.filter(published = True)
    paginated_posts = Paginator(posts, 20)

    try:
        # page/2/ ile girilmişse onu getir.
        target_page = paginated_posts.page(page)
    except EmptyPage:
        # getiremezsen anasayfaya yönlendir.
        return redirect(reverse('index_path'))
    except:
        # en son çare page değişkenini 1 kabul et.
        target_page = paginated_posts.page(1)
        


    response_dict = {
        'posts': target_page.object_list,
        'page': target_page,
        }
    
    return render(request, 'posts/index.html', response_dict)


#@cache_page(60 * 5)
def show(request, topic, slug):
    """
    Birincil anahtarı ile girilen anahtarı eşit olanı göster.
    Kaşeleme yapılıyor. 5 dakika süresince RAM'de tutulur.
    """

    post = get_object_or_404(Post, slug = slug)

    if not post.topic.slug == topic or not post.published:
        raise Http404

    response_dict = {
        'post': post,
        }

    return render(request, 'posts/show.html', response_dict)


def show_topic(request, slug):
    """
    Konu göstermede kullanılıyor.
    Seçilen konudaki bütün gönderileri listeliyor.
    """

    topic = Topic.objects.get(slug = slug)
    posts = Post.objects.filter(topic = topic)

    response_dict = {
        'posts': posts,
        'topic': topic,
        }
    
    return render(request, 'posts/show_topic.html', response_dict)
    
