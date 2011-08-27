# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from pythontr.app.links.models import Link

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
    

    def test_add_new_test(self):
        """
        """
        
        response = client.get(reverse('links:index_path'))
        self.assertEqual(response.status_code, 200)
