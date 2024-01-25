from django.urls import path

from myapp.views import import_from_excel, talon, error, service

urlpatterns = [
    path('', import_from_excel, name='index'),
    path('talon.html', talon, name='talon'),
    path('error.html', error, name='error'),
    path('service.html', service, name='service'),
]
