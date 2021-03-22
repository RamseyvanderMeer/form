
from django.urls import path
from . import views

urlpatterns = [
    path('', views.createpost),
    path('sendjson', views.send_json, name='send_json'),
]
