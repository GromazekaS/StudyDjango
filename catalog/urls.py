from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/publish/', views.PublishProductView.as_view(), name='product_publish'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # path ('', views.catalog_view, name='home'),
    # path ('menu', views.menu, name='menu'),
    path ('contacts/', views.ContactsView.as_view(), name='contacts'),
    # path ('product/list/', views.products_list_view, name='products_list'),
    # path ('product/info/<int:pk>', views.product_details, name='product_info'),
]