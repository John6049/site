from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def thread(request):
	posts = Post.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
	context = {'posts':posts}
	return render(request, 'forum/thread.html',context)

def post_new(request):
	form = PostForm()
	return render(request, 'forum/new_thread.html',{'form',form})