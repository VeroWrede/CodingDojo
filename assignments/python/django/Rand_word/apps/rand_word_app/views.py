# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def welcome(req):
    return render(req, 'rand_word_app/temp_master.html')
