from django.urls import path

from students import views

urlpatterns = [
    path('', views.StudentView.as_view()),
    path('<int:student_id>/', views.StudentDetailView.as_view()),
]