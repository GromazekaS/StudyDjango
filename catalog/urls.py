from django.urls import path

from . import views

urlpatterns = [
    path ('', views.catalog_view, name='home'),
    path ('menu', views.menu, name='menu'),
    path ('contacts/', views.send_callback, name='contacts'),
    path ('product/list/', views.product_list_view, name='product_list'),
    path ('product/info/<int:pk>', views.product_details, name='product_info'),
]