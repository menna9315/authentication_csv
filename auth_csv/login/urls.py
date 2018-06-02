from django.conf.urls import include, url
from login import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^login$',views.login),
]