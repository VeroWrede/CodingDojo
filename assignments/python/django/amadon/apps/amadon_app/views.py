# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item


def index(req):
    content = {
        'items': Item.objects.all()

    }
    return render(req, 'amadon_app/index.html')
