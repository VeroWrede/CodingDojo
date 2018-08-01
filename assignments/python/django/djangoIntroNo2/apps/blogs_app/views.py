# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'blogs_app/index.html')

def new(request):
	return render(request, 'blogs_app/new.html')

def create(request):
	return render(request, 'blogs_app/create.html')

def show(request, blog_num):
	context = {
		'blog_num' : blog_num
	}
	return render(request, 'blogs_app/show.html', context)

def edit(request, blog_num):
	context = {
		'blog_num' : blog_num
	}
	return render(request, 'blogs_app/edit.html', context)

def delete(request, blog_num):
	context = {
		'blog_num' : blog_num
	}
	return render(request, 'blogs_app/delete.html', context)	 