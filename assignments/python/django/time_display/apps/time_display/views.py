# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime

# Create your views here.
def index(request):
	current_datetime = {
	'current_time': datetime.now().time(),
	'current_date': datetime.now().date()
	}
	return render(request, 'time_display/index.html', current_datetime)