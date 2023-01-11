from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


app_name="account"

urlpatterns=[
    # path('change_password',ChangePasswordView.as_view(),name='change_password'),
    # path('check_if_account_exists',does_account_exist_view,name='check_if_account_exists'),
    path('register',views.registration_view,name='register'),
    path('login',obtain_auth_token,name='login'),
    # path('login',ObtainAuthTokenView.as_view(),name='login'),
    path('properties/update',views.update_account_view,name='update'),
    path('properties',views.account_properties_view,name='properties'),
]