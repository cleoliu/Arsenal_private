from django.urls import path

from . import views

app_name = 'case' 
urlpatterns = [
    path('', views.cases, name='case'),
]
