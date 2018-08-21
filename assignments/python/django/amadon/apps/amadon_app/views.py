# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(req):
    return render(req, 'amadon_app/index.html')
