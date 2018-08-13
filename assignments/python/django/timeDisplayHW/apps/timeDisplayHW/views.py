# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime

def index(req):
    data = {
        'current_time' : datetime.now().time(),
        'current_date' : datetime.now().date()
    }
    return render(req, 'time_app_masters/master.html', data)
