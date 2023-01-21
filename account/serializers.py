from account.models import Account
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):

        password2 =serializers.CharField(style={'input_type':'password'},write_only=True)

        class Meta:
            model = Account
            fields = ['email', 'username', 'password','password2']
            extra_kwargs={
                'password':{'write_only':True}
            }

        def save(self):
            account=Account(
                email=self.validated_data['email'].lower(),
                username=self.validated_data['username'].lower(),
            )
            password=self.validated_data['password']
            password2=self.validated_data['password2']

            if password != password2:
                raise serializers.ValidationError({'password':'Passwords must match'})
            account.set_password(password)
            account.save()
            return account

#Serilaizer for GETTing and Changing account properties
class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['pk','username','email']

class ChangePasswordSerializer(serializers.Serializer):
	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)
