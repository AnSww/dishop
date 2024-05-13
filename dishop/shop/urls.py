from django.urls import path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView

app_name = 'shop'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('', HomePageView.as_view(), name='home'),
]