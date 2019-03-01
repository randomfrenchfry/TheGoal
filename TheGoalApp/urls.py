from django.urls import path

from . import views

urlpatterns = [
    path(r'^home/$', views.home, name='home'),
    path(r'^profile/$', views.profile, name="profile"),
]
