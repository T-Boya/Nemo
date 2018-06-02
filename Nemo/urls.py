from django.conf.urls import url
from Nemo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^room/(?P<slug>[-\w]+)-(?P<id>\d+)/$', views.room, name='room'),    
]