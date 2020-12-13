from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
]
