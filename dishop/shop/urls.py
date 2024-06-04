from django.urls import path, include
from .views import HomePageView, CustomersListView, product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('list/', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),

    path('cart/', include('cart.urls', namespace='cart')),

    path('customers', CustomersListView.as_view(), name='customers'),


    path('', HomePageView.as_view(), name='home'),
]
