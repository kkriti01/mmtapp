from rest_framework import serializers


from .models import Airports


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airports
