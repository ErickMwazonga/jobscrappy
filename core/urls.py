from django.conf.urls import url
from django.contrib import admin

from . import views
from .views import IndexView, ScrapeListView

app_name = 'core'

urlpatterns = [
    url(r'^api', views.api, name='api'),
    url(r'^scrape-brighter-monday', ScrapeListView.as_view(), name='scrape'),
    url(r'^', IndexView.as_view(), name='index'),
]
