from django.urls import path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView, product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('list/', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),



    path('search', SearchView.as_view(), name='search'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),


    path('', HomePageView.as_view(), name='home'),
]
