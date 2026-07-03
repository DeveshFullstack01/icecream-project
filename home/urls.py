from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Icecream Admin"
admin.site.site_title = "Icecream Admin Portal"
admin.site.index_title = "Welcome to Icecream"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
]