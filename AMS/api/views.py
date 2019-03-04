from rest_framework import generics

from api.serializers import ServiceSerializer
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


