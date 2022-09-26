
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Bussiness as bussiness, UserBussiness
import json


class Bussiness(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = request.user
        b = {}
        if (id > 0):
            b = bussiness.objects.filter(id=id).values()
        else:
            b = bussiness.objects.values()
        return Response({"message": 'Bussines consulted success.', 'bussines': b})

    def post(self, request):
        body = json.loads(request.body)
        user = request.user
        b = bussiness.objects.create(
            name=body['name'], nit=body['nit'], address=body['address'])
        UserBussiness.objects.create(bussiness=b, user=user)
        return Response({"message": 'Bussines created success.'})

    def put(self, request, id):
        body = json.loads(request.body)
        b = bussiness.objects.get(id=id)
        b.name = body['name']
        b.nit = body['nit']
        b.address = body['address']
        b.save()
        return Response({"message": 'Bussines updated success.'})

    def delete(self, request, id):
        b = bussiness.objects.get(id=id)
        b.delete()
        return Response({"message": 'Bussines deleted success.'})
