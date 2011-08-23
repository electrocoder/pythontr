# -*- coding: utf-8 -*-

from django.db import models


class Label(models.Model):
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


    class Meta:


        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"


        
