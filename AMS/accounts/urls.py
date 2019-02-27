from django.urls import path

from accounts.views import ChangePasswordView, Dashboard
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('changepassword/', ChangePasswordView.as_view(), name='change-password'),

]
