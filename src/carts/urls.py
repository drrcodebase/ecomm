from django.conf import settings
from django.conf.urls import url
from django.urls import path

from carts.views import (
    cart_home,
    cart_update,
    )

app_name='carts'

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name="update"),

]
