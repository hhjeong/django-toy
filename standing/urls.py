from django.conf.urls import patterns, url

from standing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='standing'),
)

