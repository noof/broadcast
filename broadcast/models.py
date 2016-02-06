from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

"""class GroupMeAPI(models.Model):
	token_text = models.CharField(max_length=200)
	def __str__(self):
		return self.token_text"""

class Token(models.Model):
	token_text = models.CharField(max_length=200)
	def __str__(self):
		return token_text

class Group(models.Model):
	#groupmeapi = models.ForeignKey(GroupMeAPI, on_delete=models.CASCADE, null=True)
	group_name = models.CharField(max_length=200)
	group_id = models.CharField(max_length=200, null=True)
	active = models.BooleanField(default=False)
	def __str__(self):
		return self.group_name

class TwitterKeys(models.Model):
	consumer_key = models.CharField(max_length=200)
	consumer_secret = models.CharField(max_length=200)
	access_token_key = models.CharField(max_length=200)
	access_token_secret = models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	screen_name = models.CharField(max_length=200, null=True)