import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from django.shortcuts import render, redirect
from django.views import View

from main.models import Service


class MainPageView(View):

    def get(self, request):

        pool = list(Service.objects.all())
        random.shuffle(pool)
        service_list = pool[:3]
        return render(request, "main/index.html", {"service_list": service_list})


class AboutView(View):

    def get(self, request):
        return render(request, "main/about.html")


class ContactView(View):

    def get(self, request):
        return render(request, "main/contact.html")


class Dashboard(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "main/__dashboard__.html")


class ServicesView(View):

    def get(self, request):
        services = Service.objects.all()
        return render(request, "main/services.html", {'services': services})


class ServicesDetailsView(View):

    def get(self, request, **kwargs):
        if request.method == 'GET':
            try:
                idik = request.GET['id']
                service = Service.objects.get(id=idik)
                return render(request, "main/services_details.html", {'service': service})
            except KeyError:
                try:
                    idik = int(kwargs['id'])
                    service = Service.objects.get(id=idik)
                    return render(request, "main/services_details.html", {'service': service})
                except KeyError:
                    raise('Error occured!')
        else:
            raise Http404

