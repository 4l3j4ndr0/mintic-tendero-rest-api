
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Customer, Bussiness as bussiness
import json


class Customers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        customer = {}
        if (id > 0):
            customer = Customer.objects.filter(id=id).values()
        else:
            customer = Customer.objects.values()
        return Response({"message": 'Customer consulted success.', 'customer': customer})

    def post(self, request):
        body = json.loads(request.body)
        b = bussiness.objects.get(id=body['bussiness_id'])
        Customer.objects.create(
            name=body['name'], last_name=body['last_name'], cellphone=body['cellphone'], bussiness=b)
        return Response({"message": 'Customer created success.'})

    def put(self, request, id):
        body = json.loads(request.body)
        customer = Customer.objects.get(id=id)
        customer.name = body['name']
        customer.last_name = body['last_name']
        customer.cellphone = body['cellphone']
        customer.save()
        return Response({"message": 'Customer updated success.'})

    def delete(self, request, id):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response({"message": 'Customer deleted success.'})
