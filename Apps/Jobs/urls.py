from django.urls import path

from . import views

urlpatterns = [
    path('jobs/', views.jobs_render),
    path('jobs/set_jobs/', views.set_jobs),
]