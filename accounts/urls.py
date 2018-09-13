from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.UserView.as_view(), name='auth_register'),
    path('login/', views.TokenView.as_view(), name='gettoken'),
]
