# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

form django palce import messages to display errors 

def index(request):
	context = {
		'blogs_posts' : Blog.object.all()
	}
	return render(request, 'blogs_app/index.html', context)

def new(request):
	return render(request, 'blogs_app/new.html')

def create(request):
	if request.method == 'POST':
		valid, response = Blog.objects.Validate_andCreate_post(request.POST)
		if not valid:
			messages.error(error)
			return redirect('/new')
		do blabla
	return redirect('/')
	Blog.Validate_andCreate_post
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