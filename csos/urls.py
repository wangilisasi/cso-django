from django.urls import path
from . import views
from django.conf import settings

app_name='csos'

urlpatterns = [
    path('csos/', views.get_cso),
    path('add/', views.add_cso),
    path('update/<int:pk>',views.update_cso),
    path('delete/<int:pk>',views.delete_cso),
    path('list/', views.APICsoListView.as_view())
]