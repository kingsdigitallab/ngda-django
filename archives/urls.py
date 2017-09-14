# from django.conf import settings
# from django.conf.urls import include, url
from django.conf.urls import url
# from django.contrib import admin
from archives.views import home

urlpatterns = [
    url(r'', home, name='home_page'),
]
