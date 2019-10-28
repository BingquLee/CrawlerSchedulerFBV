<<<<<<< HEAD
from django.urls import path

# from . import views
from Apps.Users import views

urlpatterns = [
    # path('', views.add_users),
    path('add_user/', views.add_users),
    path('delete_user/', views.delete_user)
]
=======
from django.urls import path

# from . import views
from Apps.Users import views

urlpatterns = [
    # path('', views.add_users),
    path('add_user/', views.add_users),
    path('delete_user/', views.delete_user),
]
>>>>>>> c7c3fae9169c3514cca359cf767c0ddb4fe4061d
