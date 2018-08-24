# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.contrib import messages

from .models import Book

def new(req):
    return render(req, 'books/new.html')

def create(req):
    valid, result = Book.objects.validate_and_create_book(req.POST)
    return redirect('books:index')

def index(req):
    context = {
        "books" : Book.objects.order_by("created_at")
    }
    return render(req, 'books/index.html', context )
