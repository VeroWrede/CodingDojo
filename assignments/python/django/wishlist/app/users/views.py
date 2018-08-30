# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User

def new(req):
    return render(req, 'users/new.html')

def create(req):
  if req.method != 'POST':
    return redirect('users:new')

  valid, result = User.objects.validate_and_create_user(req.POST)
  if not valid:
    for err in result:
      messages.error(req, err)
    return redirect('users:new')

def show(req, user_id):
    user_id = int(user_id)
    context = {
        'name': user['name'],
        'user_name': user['user_name'],
        'hired_date': user['hired_date']
    }
    return render(req, 'users:show', context)


