from django.conf.urls import url
from django.urls import re_path

from api.views import ServiceRUDView


urlpatterns = [
    re_path(r'^(?P<pk>(\d)+)/$', ServiceRUDView.as_view(), name='app-request-api'),


]
