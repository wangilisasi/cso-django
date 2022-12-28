from rest_framework import serializers
from .models import Cso
class CsoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cso
        fields=('name','description')