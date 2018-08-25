# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.core import serializers
from django.contrib import messages

from .models import User
def index(req):
    if 'user_id' not in req.session:
        return redirect('users:new')
    context = {
        "users" : User.objects.all()
    }
    return render(req, 'users/index.html', context)

def new(req):
    return render(req, 'users/new.html')

def create(req):
    if req.method != 'POST':
        return redirect('user:new')
        print req.POST
    valid, result = User.objects.validate_and_create_user(req.POST)
    if not valid:
        for err in result:
            messages.error(req, err)
        return redirect('user:new')
    
    req.session['user_id'] = result
    return redirect('user:index')

def login(req):
    if req.method != 'POST':
        return redirect('user:new')
    valid, result = User.objects.login(req.POST)
    if not valid:
        for err in result:
            message.error(req,err)
        return redirect('user:new')
    req.session['user_id'] = result
    return redirect('user:index')

def logout(req):
    req.session.clear()
    return redirect('user:index')
