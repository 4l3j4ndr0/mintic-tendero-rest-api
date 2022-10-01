
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Provider, Bussiness as bussiness
import json


class Providers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None, bussiness_id=None):
        provider = None
        if (id is not None and bussiness_id is not None):
            if (id == 0):
                provider = Provider.objects.filter(
                    bussiness_id=bussiness_id).values()
            else:
                provider = Provider.objects.filter(
                    id=id, bussiness_id=bussiness_id).values()
        return Response({"message": 'Provider consulted success.', 'provider': provider})

    def post(self, request):
        body = json.loads(request.body)
        b = bussiness.objects.get(id=body['bussiness_id'])
        Provider.objects.create(
            name=body['name'], last_name=body['last_name'], cellphone=body['cellphone'], bussiness=b)
        return Response({"message": 'Provider created success.'})

    def put(self, request, id=None):
        body = json.loads(request.body)
        if (not id):
            id = body['id']
        provider = Provider.objects.get(id=id)
        provider.name = body['name']
        provider.last_name = body['last_name']
        provider.cellphone = body['cellphone']
        provider.save()
        return Response({"message": 'Provider updated success.'})

    def delete(self, request, id, bussiness_id):
        provider = Provider.objects.get(id=id)
        provider.delete()
        return Response({"message": 'Provider deleted success.'})
