from django.conf.urls import include, url
from browser import views

#taalla esitetaan kaikki urlit joihin paasee
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^userdetails/$', views.palautadata, name='palautadata'),
]