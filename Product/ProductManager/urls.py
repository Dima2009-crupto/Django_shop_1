from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),

path('products/', views.ProductListView.as_view(), name='product_list'),
path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

path('sign_up/', views.sign_up, name='sign_up'),
path('sign_in/', views.sign_in, name='sign_in'),

# простая работа с cookie
path('cookies/', views.cookie_consent, name='cookie_consent'),
]