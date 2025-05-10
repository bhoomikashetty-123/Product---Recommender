from django.shortcuts import render
from collections import Counter
from orders.models import Order

def dashboard_view(request):
    all_orders = Order.objects.all()

    product_counter = Counter()
    for order in all_orders:
        for product in order.products.all():
            product_counter[product.name] += 1

    top_products = product_counter.most_common(5)
    labels = [name for name, _ in top_products]
    data = [count for _, count in top_products]

    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'dashboard/dashboard.html', context)
