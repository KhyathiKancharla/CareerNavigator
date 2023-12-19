from django.urls import path
from . import views
urlpatterns = [
path('student_profile_genetator_api', views.student_profile_genetator_api),
]