# -*- coding: utf-8 -*-

from django.forms import ModelForm
from pythontr.app.links.models import Link


class NewLinkForm(ModelForm):

    class Meta:

        model = Link
        exclude = ('accepted', )
