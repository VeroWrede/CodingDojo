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
        #try:
            #check if itr already exists??
        #exept:
            #errors.append('Book already in DB)
            #return (False, errors)
    
    def delete_book(self, user_id):
        return 'NEVER EVER DELETE A BOOK!!! YOU SHALL BURN IN HELL...'

class Book(models.Model):
    name = models.CharField(max_Length=100)
    Author = models.ForeignKey(Author, related_name="books")
    reviews = models.OneToOneField(Review, related_name="book_review")
    ratings_num = models.AutoField(max_lenght=100)
    ratings_avg = models.AutoField(max_Length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name