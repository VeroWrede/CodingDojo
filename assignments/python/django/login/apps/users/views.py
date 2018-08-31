# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages

from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')
  user_name = req.session['user_id']
  context = {
    'user': User.objects.get(user_name=user_name)
  }
  return render(req, 'users/index.html', context)

def create(req):
  if req.method != 'POST':
    return redirect('users:new')

  valid, result = User.objects.validate_and_create_user(req.POST)
  if not valid:
    for err in result:
      messages.error(req, err)
    return redirect('users:new')

  req.session['user_id'] = result
  return redirect('users:index')

def new(req):
    return render(req, 'users/new.html')

def show(req, user_name):
  if 'user_id' not in req.session:
    return redirect('users:new')
    
  try:
    user = User.objects.get(user_name=user_name)
    print "*"*30
    print user
    
  except:
    return redirect('users:index')

  context = {
    'name': user.name,
    'user_name': user.user_name,
    'dob': user.dob,
  }

  json_data = json.dumps(context)
  return HttpResponse(json_data, content_type="application/json", status=200)

    

