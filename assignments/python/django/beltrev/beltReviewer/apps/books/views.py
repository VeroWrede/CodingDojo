# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def create(req):
    context={
        "books" : Book.objects.all()
    }
    return render(req, 'books/create.html', context)
