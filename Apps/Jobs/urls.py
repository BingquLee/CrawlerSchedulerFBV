from django.urls import path

# from . import views
from Apps.Jobs import views

urlpatterns = [
    path('', views.jobs_render),
    path('set_jobs/', views.set_jobs),
    path('delete_job', views.delete_job),
    path('get_accounts_list', views.get_accounts_list),
    path('get_jobs', views.get_jobs)
]
