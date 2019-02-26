import random

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404

from django.shortcuts import render, redirect, get_object_or_404
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
                service = get_object_or_404(Service, id=idik)
                return render(request, "main/services_details.html", {'service': service})
            except KeyError:
                try:
                    idik = int(kwargs['id'])
                    service = get_object_or_404(Service, id=idik)
                    return render(request, "main/services_details.html", {'service': service})
                except KeyError:
                    raise('Error occured!')
        else:
            raise Http404


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main/password_change.html')

    def post(self, request):
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        u = User.objects.get(username=request.user)

        if password and confirmPassword and password == confirmPassword:
            u.set_password(password)
            update_session_auth_hash(request, u)  # doesnt log out after change
            u.save()
            text = 'Password changed'
            return render(request, 'main/password_change.html', {"text": text})
        text = 'Incorrect password'
        return render(request, 'main/password_change.html', {"text": text})

