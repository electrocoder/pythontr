# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


from pythontr.settings import MEDIA_URL

class Editor(models.Model):
    """
    Gönderileri yazan editörler için oluşturulmuş model.
    
    Henüz taslak aşamasında.
    """
    

    user = models.OneToOneField(
        User,
        verbose_name = "Üye",
        )

    photo = models.ImageField(
        upload_to = 'user-images',
        verbose_name = "Grafik",
        )
    
    web = models.CharField(
        max_length = 75,
        verbose_name = "Web sitesi",
        blank = True,
        null = True,
        )
    bio = models.TextField(
        verbose_name = "Kısa açıklama",
        blank = True,
        null = True,
        )

    def __unicode__(self):
        return self.user.username

    
    class Meta:
        ordering = ['-user__username']
        verbose_name = "Editör"
        verbose_name_plural = "Editörler"
