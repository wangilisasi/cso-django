from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Cso
from .serializer import CsoSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

@api_view(['GET',])
@permission_classes([AllowAny])
def get_cso(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        cso = Cso.objects.all()
        serializer = CsoSerializer(cso, many=True)
        return Response(serializer.data)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def add_cso(request):
    if request.method == 'POST':

        data=request.data
        print(data)
        data['author'] = request.user.pk
        print(data)

        serializer = CsoSerializer(data=data)

        data_r = {}
        if serializer.is_valid():
            cso=serializer.save()
            # data_r['response'] = "Created succesfully"
            # data_r['pk'] = cso.pk
            # data_r['title'] = cso.name
            # data_r['body'] = cso.description
            # data_r['username'] = cso.author.username
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_cso(request,pk):
#     try:
#         cso=Cso.objects.get(pk=pk)
#         print(cso.name)
#         print(cso.description)
#     except Cso.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'PUT':
#         serializer = CsoSerializer(cso, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # if request.method == 'PUT':
#     #     serializer = CsoSerializer(cso)
#     #     data = {}
#     #    if serializer.is_valid():
#     #         print("Valiiiid")
#     #     #     serializer.save()
#     #     #     data['success']="Update succesful"
#     #     #     return Response(data)
#     #         return Response(serializer.data)
#         #return Response(status=status.HTTP_400_BAD_REQUEST)
#         # return Response(serializer.data)

@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def update_cso(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        cso = Cso.objects.get(pk=pk)
    except Cso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    user=request.user
    print(user)
    print(cso.author)
    if cso.author != user:
        return Response({"response":"You are not permitted to edit that"})

    if request.method == 'PUT':
        serializer = CsoSerializer(cso, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']="Succesfully updated blogpost"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cso(request,pk):
    try:
        cso = Cso.objects.get(pk=pk)
    except Cso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if cso.author != user:
        return Response({"response":"You are not allowed to delete that"})

    if request.method == 'DELETE':
        operation=cso.delete()
        data={}
        if operation:
            data["success"]="Deleted Succsfully"
        else:
            data["faulure"]="Failed to delete record"
        return Response(data=data)

class APICsoListView(ListAPIView):
    queryset=Cso.objects.all()
    serializer_class=CsoSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(AllowAny,)
    pagination_class=PageNumberPagination
    filter_backends=(SearchFilter,OrderingFilter,)
    search_fields=['name','description','author__username']



    
