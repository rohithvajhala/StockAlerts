from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name="home_page"),
    path('home/', views.home_view, name='home_page'),
    path('update_quotes/', views.update_quotes, name='update_quotes'),
    path('stock_details/<str:name>/', views.stock_details_view, name='stock_details'), ]
