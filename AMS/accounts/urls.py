from django.urls import path

from accounts.views import ChangePasswordView, Dashboard, EditProfileView
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('changepassword/', ChangePasswordView.as_view(), name='change-password'),
    path('editprofile/', EditProfileView.as_view(), name='edit-profile'),

]
