from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.get_cso),
    path('add/', views.add_cso),
]