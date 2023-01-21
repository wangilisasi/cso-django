from django.urls import path
from . import views
from django.conf import settings

app_name='csos'

urlpatterns = [
    path('csos/', views.get_cso),
    path('create/', views.api_create_cso_view),
    path('<int:pk>/update/',views.api_update_cso_view),
    path('<int:pk>/delete/',views.delete_cso),
    path('list/', views.APICsoListView.as_view()),
    path('<int:pk>/is_author', views.api_is_author_of_blogpost)
]

