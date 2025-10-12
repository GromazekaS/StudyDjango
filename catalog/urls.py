from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # path ('', views.catalog_view, name='home'),
    # path ('menu', views.menu, name='menu'),
    path ('contacts/', views.ContactsView.as_view(), name='contacts'),
    # path ('product/list/', views.product_list_view, name='product_list'),
    # path ('product/info/<int:pk>', views.product_details, name='product_info'),
]