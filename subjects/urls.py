from django.urls import path

from subjects import views

urlpatterns = [
    path('', views.SubjectView.as_view()),
    path('registration/<int:subject_id>/', views.SubjectRegistrationView.as_view()),
    path('registration_modify/<int:registration_id>/', views.SubjectRegistrationDetailView.as_view()),
]