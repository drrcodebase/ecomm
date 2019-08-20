from django.conf import settings
from django.conf.urls import url
from django.urls import path

from .views import (
    SearchProductView
    )
app_name='search'
urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
