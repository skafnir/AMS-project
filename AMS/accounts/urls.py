from django.urls import path

from main.views import ChangePasswordView
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('changepassword/', ChangePasswordView.as_view(), name='change-password'),

]
