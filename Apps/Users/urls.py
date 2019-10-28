from django.urls import path

# from . import views
from Apps.Users import views

urlpatterns = [
    # path('', views.add_users),
    path('add_user/', views.add_users),
    path('delete_user/', views.delete_user)
]