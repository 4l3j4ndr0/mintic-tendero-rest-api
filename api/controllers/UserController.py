
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..models.UserBussiness import UserBussiness, Bussiness
import json


class User(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        bussinesUser = UserBussiness.objects.filter(user=user).values()
        bussines = []
        for item in bussinesUser:
            b = Bussiness.objects.filter(id=item['bussiness_id']).values()[0]
            bussines.append(b)

        data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "bussiness": bussines
        }
        return Response({"message": 'User consulted success.', 'user': data})
