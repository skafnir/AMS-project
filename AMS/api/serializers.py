from rest_framework import serializers

from main.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'pk',
            'name',
            'type_of',
            'duration',
            'price',
            'description',

            ]

    # converts to JSON
    # validation for data passed

