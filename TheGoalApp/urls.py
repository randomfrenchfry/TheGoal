from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
<<<<<<< HEAD
    path('signup/', views.signup, name='singup'),
=======
    path('profile/', views.profile, name='profile')
>>>>>>> 3cdd1154f54887111a427815c9cbe9e97d8f3240
]
