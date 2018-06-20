# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if 'surveys' not in request.session:
		request.session['surveys'] = []
	return render(request, 'survey_form/index.html')

def new_survey(request):
	if request.method == 'POST':
		new_survey = {}
		new_survey['name'] = request.POST['name']
		new_survey['location'] = request.POST['location']
		new_survey['language'] = request.POST['language']
		new_survey['comment'] = request.POST['comment']
		request.session['surveys'].append(newsurvey)
		request.session.modified = True
		#for survey in request.session['surveys']: