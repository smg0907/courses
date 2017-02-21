from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.add_course),
    url(r'^courses/destroy/(?P<id>\d+)$', views.remove_course),
    url(r'^delete$', views.delete_course),
]
