from django.urls import path

from teachers import views

urlpatterns = [
    path('', views.TeacherView.as_view()),
    path('<int:teacher_id>/', views.TeacherDetailView.as_view()),
    # path('', views.StudentView.as_view(), name='index'),
]