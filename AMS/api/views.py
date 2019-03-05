from django.db.models import Q
from rest_framework import generics, mixins

from api.serializers import ServiceSerializer, AppointmentRequestSerializer
from appointments.models import AppointmentRequest
from main.models import Service


class ServiceRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = ServiceSerializer
    # queryset = Service.objects.all()

    # search
    def get_queryset(self):
        qs = Service.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = filter(Q(name__icontains=query) | Q(description_icontains=query)).distinct()
            # filters qs and allows to check in name and description and makes them unique
        return qs
        #  eg. http://127.0.0.1:8000/api/service/?q='some search'


    # overrides lookup_field
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Service.objects.get(pk=pk)


class ServiceCreateView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = ServiceSerializer
    # permission_classes = []           everything is permitted
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

