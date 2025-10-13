from django.urls import path

from . import views

namespace = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # path ('', views.catalog_view, name='home'),
    # path ('menu', views.menu, name='menu'),
    # path ('contacts/', views.ContactsView.as_view(), name='contacts'),
    # path ('product/list/', views.product_list_view, name='product_list'),
    # path ('product/info/<int:pk>', views.product_details, name='product_info'),
]