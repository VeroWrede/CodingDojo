# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'blogs_app/index.html')

def new(request):
	return render(request, 'blogs_app/new.html')

def create(request):
	return render(request, 'blogs_app/create.html')

def show(request):
	number = { 
		'wrongNum1' : 99,
		'wrongNum2' : 84932
	}
	return render(request, 'blogs_app/show.html', number)

def edit(request):
	return render(request, 'blogs_app/edit.html')

def delete(request):
	return index(request)	 