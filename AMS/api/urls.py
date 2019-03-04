from django.urls import re_path

from api.views import ServiceRUDView, ServiceCreateView, AppointmentRequestCreateView, AppointmentRequestRUDView

urlpatterns = [
    re_path(r'^service/(?P<pk>(\d)+)/$', ServiceRUDView.as_view(), name='api-service-rud'),
    re_path(r'^service/', ServiceCreateView.as_view(), name='api-service-create'),
    re_path(r'^appointment/(?P<pk>(\d)+)/$', AppointmentRequestRUDView.as_view(), name='api-appointment-rud'),
    re_path(r'^appointment/', AppointmentRequestCreateView.as_view(), name='api-appointment-create'),

]
