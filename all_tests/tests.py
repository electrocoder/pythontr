# -*- coding: utf-8 -*-

from django.test import TestCase

from pythontr.all_tests.documents.tests import *
from pythontr.all_tests.posts.tests import *
from pythontr.all_tests.links.tests import *
from pythontr.all_tests.code_bank.tests import *
from pythontr.all_tests.videos.tests import *
from pythontr.all_tests.users.tests import *

"""
Bütün testler bu dosyadan idare edilecek.
Tag, Topic, Post modelleri için olan testler posts/ klasörü altında.

Tag, Topic, Post
  -> posts/

Document
  -> documents/

Link
  -> links/

Code
  -> code_bank/

Video
  -> videos/

User, Editor
  -> users/
"""
