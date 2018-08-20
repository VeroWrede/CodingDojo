# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(req):
    render redirect(req, 'RegistrationForm/form.html')

