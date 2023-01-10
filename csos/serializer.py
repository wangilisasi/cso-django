from rest_framework import serializers

from .models import Cso
class CsoSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model=Cso
        fields=['name','description','author','username','date_published']

    def get_username_from_author(self,cso):
        username = cso.author.username
        return username