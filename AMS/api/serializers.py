from rest_framework import serializers

from appointments.models import AppointmentRequest
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
        # specify unchangeable data, pk is here default
        read_only_fields = ['pk']

    # converts to JSON
    # validation for data passed

    def validate_name(self, value):
        qs = Service.objects.filter(name_iexact=value)
        if self.instance:                                   # excluding instance
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Name already been used")
        return value


class AppointmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRequest
        fields = [
            'pk',
            'status',
            'user',
            'services',
            'duration_total',
            'price_total',
            'date_from',
            'date_to',
            'extra_info',
            'created',

            ]
        # specify unchangeable data, pk is here default
        read_only_fields = ['user', 'created']



