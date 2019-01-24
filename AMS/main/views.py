from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class MainPageView(View):

    def get(self, request):

        return render(request, "main/index.html")
        # pool = list(JedzonkoRecipe.objects.all())
        # random.shuffle(pool)
        # recipes_list = pool[:3]
        # return render(request, "index.html", {"recipes_list": recipes_list})


class AboutView(View):

    def get(self, request):
        return render(request, "main/about.html")


class ContactView(View):

    def get(self, request):
        return render(request, "main/contact.html")


class Dashboard(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "main/__dashboard__.html")

