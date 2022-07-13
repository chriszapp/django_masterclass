from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('fill_form/', views.fill_form, name = 'fill_form'),
    path('student_list/', views.student_list, name = 'student_list'),
]