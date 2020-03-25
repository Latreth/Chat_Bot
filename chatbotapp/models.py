from django.db import models
from datetime import datetime
from django.contrib.auth.signals import user_logged_in, user_logged_out  
from django.contrib.auth.models import User
import urllib, hashlib, binascii

class Message(models.Model):
	message = models.TextField(max_length=200)
	time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.user