"""AMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include

from appointments.views import AppointmentRequestView, AppointmentsView
from main.views import MainPageView, AboutView, ContactView, Dashboard, ServicesView, ServicesDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main_page'),
    path('services/', ServicesView.as_view(), name='services'),
    re_path(r'^services/details/(?P<id>(\d)+)/$', ServicesDetailsView.as_view(), name='services-details'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('appointmentrequest/', AppointmentRequestView.as_view(), name='appointment-request'),
    path('myappointments/', AppointmentsView.as_view(), name='my-appointments'),



]
