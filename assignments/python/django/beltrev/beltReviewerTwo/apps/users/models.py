# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate_and_create_user(self, form_data):
        errors = []

        if not len(form_data['name']):
            errors.append('Must enter a user name')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('invalid email')
        if not len(form_data['password']):
            errors.append('must enter a password')
        if form_data['password'] != form_data['confirm']:
            errors.append('Passwords dont match')
        

        if errors:
            return (False, errors)
        
        try:
            existing_user = self.get(email=form_data['email'])
            errors.append('Email already exists')
            return (False, errors)
        except:
            pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
            user = self.create(
                name = form_data['name'],
                email = form_data['email'],
                pw_hash = form_data['pw_hash']
            )
    
    def validate_and_update_user(self, user_id, form_data):
        errors =[]

        if not len(form_data['name']):
            errors.append('must enter a user name')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('invalid email')
        if not len(form_data['password']):
            errors.append('Must enter a password')
        if form_data['password'] != form_data['confirm']:
            errors.append('Passwords dont match')
        
        if errors:
            return (False, errors)

        try:
            user = self.get(id=user_id)
            user.name = form_data['name']
            user.email = form_data['email']
            user.save()
            return (True, user)
        except:
            errors.append('user doenst exist')
            return (False, errors)

    def delete_user_by_user_id(self, user_id):
        try:
            user = self.get(id=user_id)
            user.delete() 
        except:
            return False       
        
    def login(self, form_data):
        errors = []

        try:
            user = self.get(email = form_data['email'])
            if not bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()):
                errors.append('wrong password or username')
                return (False, errors)
            return (True, user.id)
        except:
            errors.append('wrong password or username')
            return (False, errors)



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pw_hash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    objects = UserManager()

def __repr__(self):
    return "<User.object: {}".format(self.name)

