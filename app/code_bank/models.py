# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from pythontr.app.posts.models import Tag


class Code(models.Model):
    """
    Kodları depolamak için kullanılıyor.

    Kodlar etiketlenebiliyor.

    'accepted' alanı kodun kabul edilip edilmediğini
    depolıyor.


    # get_absolute_url testi
    
    """

    sender = models.ForeignKey(
        User,
        verbose_name = "Gönderen",
        help_text = "Gönderen üye"
        )

    title = models.CharField(
        max_length = 255,
        verbose_name = "Başlık",
        unique = True,
        )

    slug = models.SlugField(
        verbose_name = "Link",
        help_text = "Bu alan otomatik olarak oluşturulur.",
        unique = True,
        )

    code = models.TextField(
        verbose_name = "İçerik",
        )

    accepted = models.BooleanField(
        verbose_name = "Kod kabul edildi mi?",
        default = False,
        )

    tags = models.ManyToManyField(
        Tag,
        verbose_name = "Etiketler",
        )

    updated_at = models.DateTimeField(
        verbose_name = "Güncellendiğinde",
        auto_now = True,
        )

    created_at = models.DateTimeField(
        verbose_name = "Yaratıldığında",
        auto_now_add = True,
        )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # güncellenmeli !
        return '/'

    class Meta:


        verbose_name = "Kod"
        verbose_name_plural = "Kodlar"

        ordering = ['-created_at']


        
    
