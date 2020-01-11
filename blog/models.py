from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title=models.CharField(max_length=100)
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):

		return self.title

class Answer(models.Model):
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Post,on_delete=models.CASCADE)

	def __str__(self):

		return self.post.title