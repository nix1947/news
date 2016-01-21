from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="politics"),
	url(r'politics/$', views.politics, name="politics"),
    url(r'economy/$', views.economy, name="economy"),
	url(r'sport/$', views.sport, name="sport"),
	url(r'abroad/$', views.abroad, name="abroad"),
	url(r'technology/$', views.technology, name="technology"),
	url(r'art/$', views.art, name="art"),
	url(r'metropolitan/$', views.metropolitan, name="metropolitan"),
	url(r'interview/$', views.interview, name="interview"),
	url(r'foreignemployment/$', views.foreignemployment, name="foreignemployment"),
	url(r'opinion/$', views.opinion, name="opinion"),
	url(r'blog/$', views.blog, name="blog"),
	url(r'health/$', views.health, name="health"),
	url(r'education/$', views.education, name="education"),
	url(r'society/$', views.society, name="society"),
	url(r'videos/$', views.videos, name="videos"),
	url(r'lifestyle/$', views.lifestyle, name="lifestyle"),
	url(r'friday/$', views.friday, name="friday"),
	url(r'saturday/$', views.saturday, name="saturday"),
	url(r'junkiri/$', views.junkiri, name="junkiri"),
]



















































































































































































