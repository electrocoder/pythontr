# -*- coding: utf-8 -*-

from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

client = Client()

class UserTest(TestCase):


    def setUp(self):
        self.user = User.objects.create(username = 'test', password = '1234', email = 'test@test.com')


    def test_show_profile_page(self):
        """
        Profil gösterme testi.
        """

        response = client.get(reverse('users:profile_path', args=[self.user.username]))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, self.user.username)
        
