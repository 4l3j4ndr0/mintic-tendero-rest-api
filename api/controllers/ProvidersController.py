
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Provider, Bussiness as bussiness
import json


class Providers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        provider = {}
        if (id > 0):
            provider = Provider.objects.filter(id=id).values()
        else:
            provider = Provider.objects.values()
        return Response({"message": 'Provider consulted success.', 'provider': provider})

    def post(self, request):
        body = json.loads(request.body)
        b = bussiness.objects.get(id=body['bussiness_id'])
        Provider.objects.create(
            name=body['name'], last_name=body['last_name'], cellphone=body['cellphone'], bussiness=b)
        return Response({"message": 'Provider created success.'})

    def put(self, request, id):
        body = json.loads(request.body)
        provider = Provider.objects.get(id=id)
        provider.name = body['name']
        provider.last_name = body['last_name']
        provider.cellphone = body['cellphone']
        provider.save()
        return Response({"message": 'Provider updated success.'})

    def delete(self, request, id):
        provider = Provider.objects.get(id=id)
        provider.delete()
        return Response({"message": 'Provider deleted success.'})
