
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Sell, Bussiness as bussines
import json

class Sell_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        Sell_detail = {}
        if(id>0):
            Sell_detail = Sells_detail.objects.filter(id=id).values()
        else:
            sell = Bussiness.objects.values()

        return Response({"message": 'Sell detail  consulted success.', 'customer': sell})

    def post(self, request):
        body = json.loads(request.body)
        s = Sell.objects.get(id=body['sells_id'])
        p = Product.objects.get(id=body['producto_id'])

        Sell_detail.objects.create(

            cantidad = body['cantidad'],
            iva = body['iva'],
            subtotal = body['subtotal'],
            producto = p,
            sell = s
        )

        return Response({"message": 'Sell_detail created success.'})

    def put(self, request, id):
        body = json.loads(request.body)
        sell_detail = Sell_detail.objects.get(id=id)

        sell_detail.cantidad = body['cantidad'],
        sell_detail.iva = body['iva'],
        sell_detail.subtotal = body['subtotal']

        sell_detail.save()
        return Response({"message": 'Seller_detail updated success.'})

    def delete(self, request, id):
        sell_detail = Sell_detail.objects.get(id=id)
        sell_detail.delete()
        return Response({"message": 'Seller_detail deleted success.'})