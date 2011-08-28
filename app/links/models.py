# -*- coding: utf-8 -*-

from django.db import models


class Link(models.Model):
    """
    Linkleri tutmak için kullanılan model.
    Örnek link <a href='(3)' (2)>(1)</a>

    'visible_name' alanı görünür ismi tutar.
    Numara 1'e gider.
    
    'open_in_new_tab' alanı linkin yeni sekmede açılıp açılmayacağını
    tutar. Eğer doğruysa 'target=_blank' yerleştirir 2 numaralı alana.

    'url' alanı linkin gerçek yolunu tutar. 3 numaralı alana yerleştirilir.       
    """
    email = models.EmailField(
        verbose_name = "Ekleyen email",
        help_text = "Güvenlik için önemli",
        )

    visible_name = models.CharField(
        max_length = 255,
        verbose_name = "Görünür isim",
        help_text = "Link için görünür isim giriniz.",
        unique = True,
        )

    open_in_new_tab = models.BooleanField(
        verbose_name = "Yeni sekmede aç",
        help_text = "Link yeni sekmede açılsın mı?",
        default = True,
        )

    url = models.CharField(
        max_length = 255,
        verbose_name = "Gerçek adres",
        help_text = "http://www.djangoproject.com/ gibi",
        )
    
    accepted = models.BooleanField(
        verbose_name = "Link kabul edildi mi?",
        default = False,
        )
    
    def __unicode__(self):
        return self.visible_name

    def get_absolute_url(self):
        return '/'

    def insert_target(self):
        """
        Template de kullanılmak üzere düşünüldü.
        Şöyle;
        <a href="{{ link.url }}" {{ link.insert_target }}>{{ link.visible_name }}</a>
        """

        if self.open_in_new_tab:
            return "target=_blank"
        else:
            return ""

    class Meta:


        verbose_name = "Link"
        verbose_name_plural = "Linkler"        
    
