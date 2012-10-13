from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from ast import literal_eval as le

urlpatterns = patterns("",
    url(r"^$", 'nltk_web.views.home', name='home'),
    url(r"^count/", 'nltk_web.views.count', name='count'),
)
