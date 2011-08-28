# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from pythontr.app.links.models import Link
from pythontr.app.links.forms import NewLinkForm

client = Client()

class LinkTest(TestCase):


    def setUp(self):

        self.link1 = Link.objects.create(
            visible_name = 'link 1',
            open_in_new_tab = False,
            url = 'http://google.com/',
            accepted = True,
            )
        
        self.link2 = Link.objects.create(
            visible_name = 'link 2',
            open_in_new_tab = True,
            url = 'http://google.com/',
            accepted = True,
            )


        self.link3 = Link.objects.create(
            visible_name = 'link 3',
            open_in_new_tab = False,
            url = 'http://google.com/',
            accepted = False,
            )

    def test_show_links_page(self):
        """
        Linklerin listelendiği sayfayı test ediyor.
        """

        response = client.get(reverse('links:index_path'))
        context = response.context

        self.assertEqual(response.status_code, 200)
        
        self.assertTrue(context['links'][0].accepted)
        self.assertTrue(context['links'][1].accepted)

    def test_insert_target(self):
        """
        insert_target() fonksiyonu test ediliyor.
        
        eğer open_in_new_tab True ise target=_blank dönmeli
        aksi halde "" dönmeli.
        """

        self.assertEqual(self.link2.insert_target(), 'target=_blank')
        self.assertEqual(self.link1.insert_target(), '')
    

    def test_add_new_link(self):
        """
        Yeni link ekleme testi.        
        """
        
        response = client.get(reverse('links:index_path'))
        self.assertEqual(response.status_code, 200)

        response = client.post(reverse('links:new_link_path'),
                               {
                'email': 'test@hotmail.com',
                'visible_name': 'test',
                'open_in_new_tab': True,
                'url': 'http://testserver.com',
                },
                               follow = True
                               )

        self.assertEqual(response.redirect_chain[0][0], 
                         'http://testserver' + reverse('blog:index_path')
                         )
        self.assertTrue(response.context['messages'])


class NewLinkFormTest(TestCase):           
    
    
    def setUp(self):
        self.data = {
            'email': '',
            'visible_name': 'test',
            'open_in_new_tab': 1,
            'url': 'http://test.com',
            }

    def test_empty_email(self):
        """
        Email alanını boş bırakarak test et.
        """
        
        form = NewLinkForm(self.data)
        self.assertTrue(form.errors.get('email'))

        self.data['email'] = 'test@test.hotmail.com'
        form = NewLinkForm(self.data)
        
        self.assertFalse(form.errors.get('email'))
        
        
    def test_empty_visible_name(self):
        """
        Görünür alanı boş bırakmayı test et.
        """
        
        self.data['visible_name'] = ''
    
        form = NewLinkForm(self.data)
        
        self.assertTrue(form.errors.get('visible_name'))

        self.data['visible_name'] = 'test'
        form = NewLinkForm(self.data)
        
        self.assertFalse(form.errors.get('visible_name'))
