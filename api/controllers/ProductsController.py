
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Product, Provider, Bussiness as bussiness
import json


class Products(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None, bussiness_id=None):
        product = None
        if (id is not None and bussiness_id is not None):
            if (id == 0):
                product = Product.objects.filter(
                    bussiness_id=bussiness_id).values()
            else:
                product = Product.objects.filter(
                    id=id, bussiness_id=bussiness_id).values()
        return Response({"message": 'Product consulted success.', 'product': product})

    def post(self, request):
        body = json.loads(request.body)
        b = bussiness.objects.get(id=body['bussiness_id'])
        p = Provider.objects.get(id=body['provider_id'])
        Product.objects.create(
            product=body['product'],
            description=body['description'],
            bar_code=body['bar_code'],
            buy_price=body['buy_price'],
            sell_price=body['sell_price'],
            stock=body['stock'],
            apply_iva=body['apply_iva'],
            send_alert=body['send_alert'],
            bussiness=b,
            provider=p
        )
        return Response({"message": 'Product created success.'})

    def put(self, request, id=None):
        body = json.loads(request.body)
        if (not id):
            id = body['id']
        product = Product.objects.get(id=id)
        product.product = body['product'],
        product.description = body['description'],
        product.bar_code = body['bar_code'],
        product.buy_price = body['buy_price'],
        product.sell_price = body['sell_price'],
        product.stock = body['stock'],
        product.apply_iva = body['apply_iva'],
        product.send_alert = body['send_alert'],
        product.save()
        return Response({"message": 'Product updated success.'})

    def delete(self, request, id, bussiness_id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"message": 'Product deleted success.'})
