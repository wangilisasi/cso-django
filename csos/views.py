from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cso
from .serializer import CsoSerializer
# Create your views here.

@api_view(['GET'])
def get_cso(request):
    cso = Cso.objects.all()
    serializer = CsoSerializer(cso, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_cso(request):
    serializer = CsoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
