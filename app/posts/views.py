# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page
from django.http import Http404

from pythontr.app.posts.models import Post, Topic, Tag

#@cache_page(30)
def index(request, page=1):
    
    posts = Post.objects.filter(published = True)
    paginated_posts = Paginator(posts, 20)

    try:
        # page/2/ ile girilmişse onu getir.
        target_page = paginated_posts.page(page)
    except EmptyPage:
        # getiremezsen /page/1 adresine yönlendir.
        return redirect(reverse('posts:index_path_page', args=(1, )))


    response_dict = {
        'posts': target_page.object_list,
        'page': target_page,
        }
    
    return render(request, 'posts/index.html', response_dict)


#@cache_page(60 * 5)
def show(request, topic, slug):
    """
    Gönderi göstermede kullanılıyor.
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
    


def show_posts_with_tag(request, slug):
    """
    Verilen slug ile etiketlenene gönderileri ( Post modeli)
    buluyor.
    """
    
    try:
        tag = get_object_or_404(Tag, slug = slug)
        posts = Post.objects.filter(tags__slug__contains = slug)
    except:
        raise Http404

    response_dict = {
        'posts': posts,
        'tag': tag,
        }
    
    return render(request,
                  'posts/show_posts_with_tag.html', 
                  response_dict
                  )
    
    
