# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from ..authors.models import Author
#from ..reviews.model import Review



class BookManger(models.Manager):
    def validate_and_create_book(self, form_data):
        errors = []

        if not len(form_data['title']):
            errors.append('Must specify a title!')
        if not len(form_data['author']):
            errors.append('Must specify an author!')
        if not form_data['title']:
            errors.append('Must specify a title!')
         
            #more validiation
        
        if errors:
            return (False, errors)
        else:
            book = self.create(
                title = form_data['title'],
                author = form_data['author'],
               # review = form_data['review'],
                rating = int(form_data['rating'])
            )
            return (True, book)

    def delete_book(self, user_id):
        return 'NEVER EVER DELETE A BOOK!!! YOU SHALL BURN IN HELL...'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    objects = BookManger()

def __repr__(self):
    return "<Book object: {} {} ".format(self.title, self.author)