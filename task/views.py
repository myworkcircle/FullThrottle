from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,ActivityPeriodsSerializer
from .models import User,ActivityPeriods
import datetime
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


# fetching details usinf listapiview
class FetchDetails(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self,request,format=None):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response({'ok':True,'members':serializer.data})








