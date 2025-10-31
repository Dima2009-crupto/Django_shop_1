from django.urls import path
from .views import ProductListView
from . import views


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add_product/', views.add_product, name='add-product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete-product'),
]