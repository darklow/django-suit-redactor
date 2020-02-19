from django.conf.urls import include
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path("admin/", include(admin.site.urls)),
]
