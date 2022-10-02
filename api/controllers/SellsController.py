
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Sell, Bussiness as bussines
import json

class Sell(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        sell = {}
        if(id>0):
            sell = Sell.objects.filter(id=id).values()
        else:
            sell = Bussiness.objects.values()

        return Response({"message": 'Sell consulted success.', 'customer': sell})

    
    def post(self, request):
        body = json.loads(request.body)
        b = Bussiness.objects.get(id=body['bussiness_id'])
        c = Customer.objects.get(id=body['customer_id'])

        Sell.objects.create(
            subtotal=body['subtotal'],
            discount=body['discount'],
            discount_concept=body['discount_concept'],
            total=body['total'],
            date=body['date'],
            bussiness = b,
            customer = c
        )

        return Response({"message": 'Sell created success.'})

    
    def put(self, request, id):
        body = json.loads(request.body)
        sell = Sell.objects.get(id=id)

        sell.subtotal = body['subtotal']
        sell.discount = body['discount']
        sell.discount_concept = body['discount_concept']
        sell.total = body['total']
        sell.date = body['date']
        sell.save()
        return Response({"message": 'Seller updated success.'})


    def delete(self, request, id):
        sell = Sell.objects.get(id=id)
        sell.delete()
        return Response({"message": 'Seller deleted success.'})