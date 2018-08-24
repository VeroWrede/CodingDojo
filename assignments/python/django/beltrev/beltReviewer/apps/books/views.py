# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 

from .models import Book

def new(req):
    return render(req, 'books/create.html')

def create(req):
    return redirect('books:index')

def index(req):
    context = {
        "books" : Book.objects.all()
    }
    return render(req, 'books/index.html', context )