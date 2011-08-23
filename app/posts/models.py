# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Blog için etiket modeli.
    """


    title = models.CharField(
        verbose_name = "Başlık",
        max_length = 100,
        unique = True,
        )

    slug = models.SlugField(
        verbose_name = "Link",
        )

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_posts_with_tag_path', args=(self.slug, ))

    class Meta:


        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"


class Topic(models.Model):
    """
    Blog için konu modeli.
    title, slug, description alanları vardır.
    /django/post/1/ veya /flask/post/15/ gibi bir url ile kullanılabilir.
    """

    title = models.CharField(
        max_length = 255,
        verbose_name = "Başlık",
        help_text = "Konu başlığı",
        unique = True,
        )

    slug = models.SlugField(
        verbose_name = "Link",
        )

    description = models.TextField(
        verbose_name = "Açıklama",
        help_text = "Bu alana kısa bir açıklama giriniz."
        )

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_topic_path', kwargs={'slug': topic.slug})


    class Meta:


        verbose_name = "Konu"
        verbose_name_plural = "Konular"

        ordering = ['title']


class Post(models.Model):
    """
    Blog için post modeli.
    'sender' gönderiyi kimin yazdığını tutar.
    'title' alanı başlık için kullanılır.
    'slug' ise insancıl url için kullanılır.
    'topic' gönderinin ait olduğu konuyu tutar.
    'title' "bu bir gönderi" ise 'slug' 
    "bu-bir-gonderi" oluyor.
    
    'content' yazının ana kısmı. Yazı burada tutuluyor.
    'published' gönderinin yayınlanıp yayınlanmadığı tutar.
    
    'has_code' gönderinin içinde kod olup olmadığını tutar.
    eğer seçilirse, yazı yayınlanırken Google code renklendirme
    javascript kütüphanesi include edilecektir.

    'tags' gönderinin sahip olduğu etiketleri tutar.
    
    """
    
    sender = models.ForeignKey(
        User,
        verbose_name = "Gönderen üye",
        help_text = "Gönderen üyeyi seçiniz."
        )

    title = models.CharField(
        verbose_name = "Başlık",
        help_text = "Bu alana gönderi başlığı girilir.",
        max_length = 255,
        unique = True,
        )

    slug = models.SlugField(
        verbose_name = "Link",
        help_text = "Bu alan otomatik olarak oluşturulur.",
        unique = True,
        )

    topic = models.ForeignKey(
        Topic,
        verbose_name = "Konu",
        )

    content = models.TextField(
        verbose_name = "İçerik",
        help_text = "Bu alana gönderi içeriği girilir."
        )

    published = models.BooleanField(
        verbose_name = "Yayınlandı mı?",
        help_text = "Gönderinin yayınlanıp yayınlanmayacağını seçiniz.",
        default = True
        )
    
    has_code = models.BooleanField(
        verbose_name = "Kod var mı?",
        help_text = "Yazı da kod var mı? Ona göre javascript include edilecek.",
        default = False,
        )

    tags = models.ManyToManyField(
        Tag,
        verbose_name = "Etiketler",
        help_text = "Gönderinin etiketleri",
        null = True,
        blank = True,
        )

    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Yaratıldığında",
        )
    
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Güncellendiğinde",
        )
    
    
    def get_absolute_url(self):
        return reverse('show_path', kwargs = {'topic': self.topic.slug, 'slug': self.slug})
    

    def __unicode__(self):
        return self.title

    
    class Meta:

        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        # tersten sıralı olarak gelsin.
        # yani en son gönderiler en başta.
        ordering = ["-created_at"]
