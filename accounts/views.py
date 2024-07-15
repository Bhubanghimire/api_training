from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from accounts.permissions import NormalUserPermission
from rest_framework.permissions import IsAuthenticated, AllowAny


class MemberInfoViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['GET'], url_path='detail')
    def user_detail(self, request, pk=None):
        user = request.user
        serialize = UserSerializer(user).data
        return Response({"data":serialize})
    
    