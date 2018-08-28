# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, redirect, HttpResponse


def index(req):
    req.session['money'] = 0
    return render(req, 'money/index.html')


def farm(req):
    if 'money' in req.session:
        req.session['money'] += random.randint(10,20)
        context = {
            'money': req.session['money']
        }
    else:
        return HttpResponse('booooooo')
    return render(req, 'money:index', context)


def cave(req):
    if 'money' in req.session:
        req.session['money'] += random.randint(5,10)
        context = {
            'money': req.session['money']
        }
    else:
        return HttpResponse('booooooo')
    return render(req, 'money:index', context)

def house(req):
    if 'money' in req.session:
        req.session['money'] += random.randint(2,5)
        context = {
            'money': req.session['money']
        }
    else:
        return HttpResponse('booooooo')
    return render(req, 'money:index', context)

def casino(req):
    if 'money' in req.session:
        temp = random.randint(1,2)
        if temp % 2 == 0:
            req.session['money'] += random.randint(0,50)
            context = {
            'money': req.session['money']
        }
        else:
            req.session['money'] -= random.randint(0,50)
            context = {
                'money': req.session['money']
            }
    return render(req, 'money:index', context)

