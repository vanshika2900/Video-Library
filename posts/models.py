from __future__ import unicode_literals
from django.db import models
from django.db.models import Q
from django.conf import settings


# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=120)
	video=models.FileField(upload_to='videos/',blank=False,null=False)
	#slug = models.SlugField(unique=True)
	content=models.TextField(null=True,blank=True)
	publish_date = models.DateTimeField(auto_now = False,auto_now_add=False,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#class PostQuerySet(models.QuerySet):
		#def search(self,query):
			#lookup = (
              #     Q(title__icontains=query)|
                  # Q(content__icontains=query)  )
			#return self.filter(lookup)

		


	#class PostManager(models.Manager):
	#	def search(self,query=None):
	#		if query is None:
	#			return self.none()
	#		return self.search(query)

	#objects=PostManager()

	def get_absolute_url(self):
		return f"/videos/{self.title}"




