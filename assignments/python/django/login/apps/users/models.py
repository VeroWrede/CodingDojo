# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
from datetime import datetime
from ..pokes

class UserManager(models.Manager):
    def validate_and_create_user(self, form_data):
        errors = []

        if len(form_data['name']) < 3:
            errors.append(['funny name, ', form_data['name'], '!'])
        if len(form_data['user_name']) < 3:
            errors.append([form_data['user_name'], " ,that's what you call yourself!?"])
        if len(form_data['password']) < 3:
            errors.append("that ain't a password!")
        if not form_data['dob']:
            errors.append('you are not one of us, get out!') 
        if form_data['password'] != form_data['confirm']:
            errors.append("Only one password per person, that's the rule")
        if errors:
            return (False, errors)

        try:
            existing_user = self.get(user_name=form_data['user_name'])
            errors.append('User Name already exists.')
            return (False, errors)
        except:
            pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
            dob = datetime.strptime(form_data['dob'],  '%Y-%m-%d').date()
            print "*"*20
            print len(pw_hash)
            user = self.create(
                name=form_data['name'], 
                user_name=form_data['user_name'],
                dob=dob,
                pw_hash=pw_hash
            )
            print "*"*30
            print user.id
            return (True, user.id)

    # def login(req):
    #     pass  
    
    # def modify(req):
    #     pass

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    dob = models.DateField()
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    objects = UserManager()


def __str__(self):
    return self.name


