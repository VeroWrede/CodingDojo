# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class blogManager(models.Model):
	def validate_and create post(salf, form_data):
		errors = []

		if !name:
			errors.append('no name')
		
		if errors:
			return(False, errors)
		blog_post = self.create(content = form_data['content'], author = form_data['autor'])
		return (true, blog_post)

class blog(models.Model):
	owner = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	cathegory = models.CharField(max_length = 200)
	created_at = models.dateTimeField(auto_now_add = True)
	updated_at = models.dateTimeField(auto_now = True)
	objects = blogManager()
	
class blog_post(models.Model):
	author = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200)
	content = models.CharField(max_length = 1000)
	created_at = models.dateTimeField(auto_now_add)
	updated_at = models.dateTimeField(auto_now)
	blog = models.ForeignKey(blog, related_name = 'blogs')
