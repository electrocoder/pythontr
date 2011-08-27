# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


from pythontr.app.posts.models import Post, Tag, Topic


client = Client()

class PostsViewTests(TestCase):
    def setUp(self):
        """
        40 tane Post kayıdı oluştur.
        """
        self.user = User.objects.create_user(username = 'yigit',
                                             password = '1234',
                                             email = 'yigit@test.com'
                                             )

        self.topic = Topic.objects.create(
            title = 'Testi',
            slug = 'testi',
            description = 'test test test'
            )

        self.tag = Tag.objects.create(title = 'tag', slug = 'tag')

        self.post = Post.objects.create(
            sender = self.user,
            title = 'Post post post',
            slug = 'post-post-post',
            content = 'birseyler',
            has_code = False,
            published = True,
            topic = self.topic
            )

        self.post.tags.add(self.tag)
        self.post.save()
        
        for i in xrange(40):
            post = Post.objects.create(sender = self.user,
                                title = 'Test %s' % i,
                                slug = 'test-%s' % i,
                                content = 'testing %s post' % i,
                                has_code = True,
                                published = True,
                                topic = self.topic,
                                )

            
    
        
    def test_index_path(self):
        """
        Sırasıyla
        '/blog/'
        '/blog/page/1/'
        '/blog/page/2/'
        adreslerine GET ile istek gönderir.
        
        200 durum kodu gelmelidir.
        """
        
        def goto_target_page(page):
            response = client.get(reverse('blog:index_path_page', args=(page, )))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.context['posts'])

        response = client.get(reverse('blog:index_path'))        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['posts'])

        goto_target_page(1)
        goto_target_page(2)


    def test_show_post(self):
        """
        Gönderiyi gösterme testi.
        200 durum kodu gelmelidir.

        """
        
        for i in xrange(1, 40):
            post = Post.objects.get(pk = i)
            response = client.get(post.get_absolute_url())

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['post'].title, post.title)


    def test_show_topic(self):
        """
        Konuyu gösterme testi.
        """

        response = client.get(self.topic.get_absolute_url())

        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.context['topic'].title, 'Testi')
        self.assertTrue(response.context['posts'])

    def test_get_absolute_url(self):
        """
        get_absolute_url testi.
        """

        post = Post.objects.get(pk = 1)

        self.assertEqual(post.get_absolute_url(), reverse('blog:show_path', args=(post.topic.slug, post.slug)))
        self.assertEqual(post.topic.get_absolute_url(), reverse('blog:show_topic_path', args=(post.topic.slug,)))



    def test_get_tag_with_posts(self):
        """
        tag ile gönderileri gösterme testi.
        """

        response = client.get(reverse('blog:show_posts_with_tag_path', args=(self.tag.slug,)))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['posts'])


    
    def test_paginate_redirect(self):
        """
        Eğer olmayan bir sayfa girilmişse ilk sayfaya
        yönlendirilmeli.
        """
        
        response = client.get(reverse('blog:index_path_page', args=[5]), follow = True)

        self.assertEqual(response.redirect_chain[0][0], 'http://testserver' + reverse('blog:index_path_page', args=[1]))
        
