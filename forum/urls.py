from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(\d+)/$', 'forum.post.number'),
    url(r'^$', views.thread, name = 'thread'),
    url(r'^new/$', views.post_new, name = 'post_new'),
]