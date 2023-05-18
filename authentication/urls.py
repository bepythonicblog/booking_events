from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import register, email_validation_view, validate, logout_view, login_view

urlpatterns = [    
    path('register/', register, name='register'),
    path('validate/<str:uidb64>/<str:token>/', validate, name='validate'),
    path('logout/', logout_view),
    path('login/', login_view, name='login'),
]