# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..authors.models import Author
from ..reviews.model import Review

class BookManger(models.Model):
    def Validate_and_create_book(self, form_data):
        errors = []

        if not len(form_data['title']):
            errors.append('Must specify a title!')
            #more validiation
        
        if errors:
            return (False, errors)
        else:
            book = self.create(
                title = form_data['title'],
                author = form_data['author'],
                #....
            )
            return (True, book)

'''

        try:
            book = self.get(id=book_id)
            book.title = form_data['title']
            book.author = form_data['author']
            book.review = form_data['rewiev']
            book.rating = form_data['rating']
        except:
            errors.append('book doesnt exist?!')
            # i dont wanna check that??

        #try:
            #check if itr already exists??
        #exept:
            #errors.append('Book already in DB)
            #return (False, errors)
'''

    def delete_book(self, user_id):
        return 'NEVER EVER DELETE A BOOK!!! YOU SHALL BURN IN HELL...'

class Book(models.Model):
    title = models.CharField(max_Length=100)
    author = models.CharField(max_length=100)
    #reviews = models.ForeignKey(Review, related_name="book_review")
    #put this foreu key into review model
    #do i have to do reviews?
    ratings_num = models.AutoField(max_lenght=100)
    ratings_avg = models.AutoField(max_Length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name
#def __repr__(self):
    #return "<Book object: {} {} ".format(self.title, self.author)