# -*- coding: utf-8 -*-

from pythontr.settings import PATH

from django.test import TestCase, Client

from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse

client = Client()

class UserViews(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(username = 'test', password = '1234', email = 'test@test.com')


    def test_show_profile_page(self):
        """
        Profil gösterme testi.
        """

        response = client.get(reverse('users:profile_path', args=[self.user.username]))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, self.user.username)
    

    def test_login(self):
        """
        Giriş yapma testi.
        """
    
        response = client.get(reverse('users:login_path'))
        self.assertEqual(response.status_code, 200) # get ile test

        response = client.post(reverse('users:login_path'), {'username': 'test', 'password': '1234'}, follow = True)
        self.assertEqual(response.redirect_chain[0][0], 'http://testserver' + reverse('blog:index_path'))
        
        response = client.get(reverse('blog:index_path'))

        self.assertTrue(response.context['user'].username)
        self.assertEqual(response.context['user'].username, self.user.username)
    
    def test_logout(self):
        """
        çıkış yapma testi.
        """

        response = client.get(reverse('users:logout_path'), follow = True)
        self.assertEqual(response.redirect_chain[0][0], 'http://testserver' + reverse('blog:index_path'))

        self.assertFalse(response.context['user'].username)
        
        

    def test_signup(self):
        response = client.get(reverse('users:signup_path'))

        self.assertEqual(response.status_code, 200)
        
        response = client.post(reverse('users:signup_path'),
                               {
                'username': 'yeget', 
                'password1': '1234',
                'password2': '1234', # password confirmation
                'web': 'http://test.com/',
                'bio': '12312312312'
                                }, follow = True)

        self.assertEqual(response.redirect_chain[0][0],
                         'http://testserver' + reverse('blog:index_path'))
        

        with open(PATH + '/all_tests/users/lion.png', 'r') as image:
            photo = image.read()

        response = client.post(reverse('users:signup_path'),
                               {
                'username': 'resimli',
                'password1': '1234',
                'password2': '1234',
                'web': 'http://test.com/',
                'bio': '123asdadqeqweqweW',
                'photo': photo
                }, follow = True)
        
        self.assertEqual(response.redirect_chain[0][0],
                         'http://testserver' + reverse('blog:index_path'))
