from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^create/$', CreatePostView.as_view(), name='post')
]
