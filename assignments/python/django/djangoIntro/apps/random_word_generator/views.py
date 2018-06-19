# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request, data):
	return render(request, 'random_word_generator/index.html')

def generate(request):
	data = {
	'number': i,
	'word': get_random_string(length=14)
	}
	return redirect(request, 'random_word_generator/index.html')

