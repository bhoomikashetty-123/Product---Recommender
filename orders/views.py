from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from orders.models import Order

@api_view(['POST'])
def create_order(request):
    product_ids = request.data.get('product_ids', [])
    if not product_ids:
        return Response({"error": "product_ids is required"}, status=400)

    products = Product.objects.filter(id__in=product_ids)
    if not products.exists():
        return Response({"error": "No valid products found"}, status=400)

    order = Order.objects.create()
    order.products.set(products)
    order.save()
    return Response({"message": f"Order {order.id} created successfully."})
