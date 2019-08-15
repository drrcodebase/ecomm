
from django.conf import settings
from django.conf.urls import url
from django.urls import path

from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    )

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products-fbv/', product_list_view),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products-fbv/<int:pk>/', product_detail_view),

]
