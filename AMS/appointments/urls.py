from django.urls import path, re_path

from appointments.views import AppointmentRequestView, AppointmentsView, AppointmentRequestDelete


urlpatterns = [
    path('appointmentrequest/', AppointmentRequestView.as_view(), name='appointment-request'),
    path('myappointments/', AppointmentsView.as_view(), name='my-appointments'),
    re_path((r'^myappointments/delete/(?P<pk>\d+)/$'), AppointmentRequestDelete.as_view(), name='appointment-delete'),

]

