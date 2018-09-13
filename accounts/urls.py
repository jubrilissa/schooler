from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.TokenView.as_view(), name='login_user'),
]
