# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

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
		new_survey['languages'] = request.POST['languages']
		new_survey['comment'] = request.POST['comment']
		valid = True
		if new_survey['name'] == "":
			messages.error(request, ' name may not be blank')
			valid = False
		if new_survey['location'] == "":
			messages.error(request, ' location may not be blank')
			valid = False
		if new_survey['languages'] == '':
			messages.error(request, ' languages may not be blank')
			valid = False
		for survey in request.session['surveys']:
			if survey['name'] == new_survey['name']:
				messages.error(request, 'you already submitted a survey form')
				valid = False
		data = {
		'new_survey': new_survey
		}
		if valid == True:
			request.session['surveys'].append(new_survey)
			request.session.modified = True
			messages.success(request, 'survey successfully submitted')
			return render(request, 'survey_form/survey_review.html', data)
	return redirect('/survey_form')
		#for survey in request.session['surveys']: