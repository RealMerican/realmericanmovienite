from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.title_list, name='title_list'),
    url(r'^title/(?P<pk>\d+)/$', views.title_detail, name='title_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^participate/$', views.participate, name='participate'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^tv/$', views.tv, name='tv'),
    url(r'^search/$', views.search, name='search'),
    url(r'^people/$', views.people_list, name='people_list'),
    url(r'^current_datetime/$', views.current_datetime, name='current_datetime'),
]
