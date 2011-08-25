# -*- coding: utf-8 -*-

from django.db import models


class Video(models.Model):
    """
    Videoları depolamak için kullanılacak olan model.
    """

    title = models.CharField(
        max_length = 255,
        verbose_name = "Başlık",
        help_text = "Video için bir başlık yazınız",
        unique = True,
        )
    
    slug = models.SlugField(
        verbose_name = "Link",
        unique = True,
        )


    published = models.BooleanField(
        verbose_name = "Yayınlandı mı?",
        help_text = "Bu video yayınlandı mı?",
        default = True,
        )

    video = models.FileField(
        upload_to = "videos",
        verbose_name = "Video",
        help_text = "Videonun kendisi",
        null = True,
        blank = True,
        )
    
    video_link = models.CharField(
        verbose_name = "Video linki",
        max_length = 255,
        help_text = "Eğer video youtube gibi bir sitedeyse, linkini yapıştır.",
        null = True,
        blank = True,
        )

    
    description = models.TextField(
        verbose_name = "Açıklama",
        help_text = "Video için açıklama giriniz.",
        )

    
    updated_at = models.DateTimeField(
        auto_now = True,
        verbose_name = "Güncelliğinde",
        )

    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Yaratıldığında",
        )
    

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        # güncellenmeli.
        return '/'
        
    class Meta:

        
        verbose_name_plural = "Videolar"
        ordering = ['-created_at']
        
