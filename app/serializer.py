from rest_framework import serializers

from models import SensorInfo


class SensorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorInfo
        fields = ('name', 'url', 'numofparams', 'namesofparams', 'endpoints')