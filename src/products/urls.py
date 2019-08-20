
from django.conf import settings
from django.conf.urls import url
from django.urls import path

from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    ProductDetailSlugView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    )
app_name='products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name="detail"),

]
