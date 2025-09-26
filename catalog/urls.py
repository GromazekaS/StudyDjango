from django.urls import path

from . import views

urlpatterns = [
    path ('', views.catalog_view, name='home'),
    # path ('contacts/', views.contacts_view, name='contacts'),
    path ('contacts/', views.send_callback, name='contacts')
]