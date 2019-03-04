from rest_framework import generics, mixins

from api.serializers import ServiceSerializer, AppointmentRequestSerializer
from appointments.models import AppointmentRequest
from main.models import Service


class ServiceRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = ServiceSerializer
    # queryset = Service.objects.all()

    def get_queryset(self):
        return Service.objects.all()

    # overrides lookup_field
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Service.objects.get(pk=pk)


class ServiceCreateView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = ServiceSerializer
    # queryset = Service.objects.all()

    def get_queryset(self):
        return Service.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentRequestRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = AppointmentRequestSerializer
    # queryset = AppointmentRequest.objects.all()

    def get_queryset(self):
        return AppointmentRequest.objects.all()


class AppointmentRequestCreateView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = AppointmentRequestSerializer
    # queryset = AppointmentRequest.objects.all()

    def get_queryset(self):
        return AppointmentRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

