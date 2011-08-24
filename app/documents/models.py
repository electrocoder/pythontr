# -*- coding: utf-8 -*-

from django.db import models
from pythontr.settings import MEDIA_URL

class Document(models.Model):
	"""
	Django book, gibi belgeleri tutmak için yapıldı.
	name, docfile, description, image alanları vardır.
	"""
	
	
	name = models.CharField(
		max_length = 200,
		verbose_name = "Adı",
		help_text = "Belge adı",
		unique = True,
		)
		
		
	slug = models.SlugField(
		verbose_name = "Belge linki",
		help_text = "Bu alan otomatik oluşturulur.",
		unique = True,
		)
		

	docfile = models.FileField(
                upload_to = 'documents',
                verbose_name = "Dosya",
                help_text = "Dosyayı seçiniz.",
                )

	description = models.TextField(
                verbose_name = "Açıklama",
                help_text = "Açıklama giriniz.",
                )

	
        
	image = models.ImageField(
                upload_to = 'document-images',
                verbose_name = "Resim",
                help_text = "Belge için resim seçiniz.",
                null = True,
                blank = True,
                )
        

        uploaded_at = models.DateTimeField(
                verbose_name = "Yüklendiğinde",
                auto_now_add = True,
        )

        def __unicode__(self):
                return self.name


        def get_absolute_url(self):
        	# app/documents/views.py show fonksiyonunun urlsini kullan.
        	# docfile.url şeklinde ulaşabilirsin indirme linkine.
        	
                return "%s%s" % (MEDIA_URL, self.docfile)


        class Meta:
                verbose_name = "Belge"
                verbose_name_plural = "Belgeler"

                ordering = ['-uploaded_at']

	
