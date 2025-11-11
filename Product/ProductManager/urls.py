from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),

path('products/', views.ProductListView.as_view(), name='product_list'),
path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

path('signup/', views.signup, name='signup'),
path('login/', views.login_view, name='login_'),

# простая работа с cookie
path('cookies/', views.cookie_consent, name='cookie_consent'),
]