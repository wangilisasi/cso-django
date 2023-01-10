from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from account.serializers import RegistrationSerializer

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
