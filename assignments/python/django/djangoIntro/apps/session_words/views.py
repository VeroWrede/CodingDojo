# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
	if 'words' not in request.session:
		request.session['words'] = []
	return render(request, 'session_words/index.html')

def add_word(request):
	if request.method == 'POST':
		word = {
			'word': request.POST['word'],
			'time': datetime.now().time(),
			'date': datetime.now().date(),
			'color': request.POST['color'],
			'font': request.POST['font']
		}
	else:
		word = {}
	messages.error(request, 'Confirm password and password must match')
	data = {
		'new_word': word
	}
	request.session['words'].append(word)
	return render(request, 'session_words/show_words.html', data)

def show_words(request):
	return render(request, 'session_words/show_words.html')

