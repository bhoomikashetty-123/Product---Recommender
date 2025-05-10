
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order
from .models import Product
from collections import Counter

@api_view(['POST'])
def recommend_products(request):
    product_ids = request.data.get('product_ids', [])
    orders = Order.objects.filter(products__id__in=product_ids)
    recommended = Counter()

    for order in orders:
        for product in order.products.exclude(id__in=product_ids):
            recommended[product.id] += 1

    recommended_ids = [product_id for product_id, _ in recommended.most_common(5)]
    recommended_products = Product.objects.filter(id__in=recommended_ids)

    from .serializers import ProductSerializer
    return Response(ProductSerializer(recommended_products, many=True).data)
