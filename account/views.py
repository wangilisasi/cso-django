from django.shortcuts import render
from rest_framework import status
from account.models import Account
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from account.serializers import RegistrationSerializer,AccountPropertiesSerializer

# Create your views here.

@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):

	if request.method == 'POST':
		# data = {}
		# email = request.data.get('email', '0').lower()
		# if validate_email(email) != None:
		# 	data['error_message'] = 'That email is already in use.'
		# 	data['response'] = 'Error'
		# 	return Response(data)

		# username = request.data.get('username', '0')
		# if validate_username(username) != None:
		# 	data['error_message'] = 'That username is already in use.'
		# 	data['response'] = 'Error'
		# 	return Response(data)
        
		serializer = RegistrationSerializer(data=request.data)
		data ={}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			data['pk'] = account.pk
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def account_properties_view(request):
	try:
		account=request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serilaizer=AccountPropertiesSerializer(account)
		return Response(serilaizer.data)

@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def update_account_view(request):
	try:
		account=request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='PUT':
		serializer=AccountPropertiesSerializer(account,request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["response"]="Account updated succesfully"
			return Response(data=data)
		return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




# def validate_email(email):
# 	account = None
# 	try:
# 		account = Account.objects.get(email=email)
# 	except Account.DoesNotExist:
# 		return None
# 	if account != None:
# 		return email

# def validate_username(username):
# 	account = None
# 	try:
# 		account = Account.objects.get(username=username)
# 	except Account.DoesNotExist:
# 		return None
# 	if account != None:
# 		return username
