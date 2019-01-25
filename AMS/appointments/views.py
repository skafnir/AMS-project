import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.urls import reverse_lazy
from dateutil import parser
from appointments.forms import AppointmentRequestForm
from appointments.models import AppointmentRequest
from main.models import Service


class AppointmentRequestView(LoginRequiredMixin, View):

    def get(self, request):
        form = AppointmentRequestForm()
        return render(request, 'appointments/appointment_request_form.html', {'form': form})

    def post(self, request):
        form = AppointmentRequestForm(request.POST)
        user = request.user
        duration_sum = datetime.timedelta(hours=0)
        price_sum = 0
        all_serv = form['services'].value()
        for i in range(len(all_serv)):
            serv_value = Service.objects.get(id=all_serv[i])
            duration_sum += serv_value.duration
            price_sum += serv_value.price
        date_from_parsed = parser.parse(form['date_from'].value())
        date_to = date_from_parsed + duration_sum
        serv_list = list(form['services'].value())
        if form.is_valid():

            appointment = AppointmentRequest.objects.create(status=1,
                                                            user=user,
                                                            duration_total=duration_sum,
                                                            price_total=price_sum,
                                                            date_from=date_from_parsed,
                                                            date_to=date_to,
                                                            extra_info=form['extra_info'].value()
                                                            )
            appointment.services.set(serv_list)
            appointment.save()
            return redirect('dashboard')
        return render(request, 'appointments/appointment_request_form.html', {'form': form})


class AppointmentsView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        appointments = AppointmentRequest.objects.filter(user=user).order_by('-date_from')
        return render(request, "appointments/my_appointments.html", {'appointments': appointments})

