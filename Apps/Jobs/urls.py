from django.urls import path

# from . import views
from Apps.Jobs import views

urlpatterns = [
    path('', views.jobs_render),
    path('set_jobs/', views.set_jobs),
    path('delete_job', views.delete_job),
<<<<<<< HEAD
]
=======
]
>>>>>>> c7c3fae9169c3514cca359cf767c0ddb4fe4061d
