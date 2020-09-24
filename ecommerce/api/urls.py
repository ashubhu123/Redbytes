from django.conf.urls import url
from .serializers import *
from .views import *
from .api import *

urlpatterns = [
    url(r'user_list/$',Userlist.as_view(),name='All users'),
    url(r'user_list/(?P<id>\d+)/$', UserDetails.as_view(), name='One user'),
    url(r'auth/$',userauth.as_view(), name='User authentication'),
    # url(r'register/$',registration, name='User registration'),
    url(r'product_list/$',ProductList.as_view(),name='All product list'),
    url(r'product_list/(?P<id>\d+)/$', ProductDetails.as_view(), name='One product'),
    url(r'order_list/$',OrderList.as_view(),name='All orders'),
    url(r'order_list/(?P<id>\d+)/$', orderDetails.as_view(), name='One order'),
]