# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ReviewManager(models.Manager):
    def validate_and_create_review(self, form_data):
        errors = []

        if not len(form_data['message']):
            errors.append('no Empty threats!')

        try:
            user = user.objects.get(id=form_data['email'])
        except: 
            errors.append('only users may review books')

        if errors:
            return (False, errors)
        else:
            review = self.creat(message=form_data['message'], book = form_data['title'])
            return (True, review)

    def delete_review_by_id(self, user_id):
        try:
            book.self.filter(user__in=User.objects.get(id=user.id))
        except:
            erros.append('you can only delete your own reviews')
        try:
            review.self.get(id='review_id')
            review.delete()
        else:
            errors.append('oups, something went wrong')
            return (False, errors)

class Review(models.Model):
    user = models.ForeignKey(User, related_name="user_reviews")
    book = models.ForeignKey(Book, related_name="review")
    message = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

def __repr__(self):
    return "<Review object: {}"