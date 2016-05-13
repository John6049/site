from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	display = ('date_created','title','content')
	filter = ('number')
	
admin.site.register(Post, PostAdmin)