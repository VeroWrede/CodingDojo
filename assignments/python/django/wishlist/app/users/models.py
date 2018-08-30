# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    pass

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length = 100)
    pw_hash = models.CharField(max_length=100)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    objects = UserManager()

def __str__(self):
    return self.name

