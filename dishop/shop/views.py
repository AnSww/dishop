from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Customer, Order, Category, Product
from cart.forms import CartAddProductForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = "customer.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "list_of_all_orders"


class SearchView(ListView):
    template_name = "search.html"
    model = Order
    context_object_name = "list_of_all_orders"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Order.objects.filter(
            Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query)
        ).order_by('order_date').reverse()


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
