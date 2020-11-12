
from django.conf.urls import url
from .views import *
app_name="crud_app"
urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^update/(?P<pk>\w+)/$', update,name="update"),
    url(r'^delete/(?P<pk>\w+)/$',delete,name="delete"),
    url(r'add/',addd,name="addd"),

]
