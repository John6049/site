from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class PostManager(models.Manager):
	def get_queryset(self):
		qs = super(PostManager, self).get_queryset()
		return	
		
class Post(models.Model):
	url = models.URLField()
	date_created = models.DateTimeField('date created')
	#tags = models.ManyToManyField(Tag, blank=True)
	title = models.TextField('title')
	content = models.TextField('content')
	number = models.IntegerField('number',default=0)
	   
	objects = models.Manager()
	public = PostManager()
	
	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		ordering = ['-date_created']
        
	def __str__(self):
		return '%s (%s)' % (self.title, self.url)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		super(Post, self).save(*args, **kwargs)