from django.contrib import admin
from django.urls import path, include

from talons import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
