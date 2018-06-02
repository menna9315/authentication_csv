from django.conf.urls import include, url
from django.contrib import admin
from login import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include("login.urls")),
]