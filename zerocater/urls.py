# Django imports
from django.contrib import admin
from django.urls import path, include

# Project imports
from restaurants import urls

# URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
