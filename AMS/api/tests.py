import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APITestCase

from appointments.models import AppointmentRequest
from main.models import Service

User = get_user_model()


class AppointmentRequestAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testUser', email='test@test.com')
        user.set_password('somerandompassword')
        user.save()
        service = Service.objects.create(name='Service example 1',
                                         type_of='Goood one',
                                         duration='3600.0',
                                         price='450.00',
                                         description='Best price / time value!'
                                        )
        appointment_request = AppointmentRequest.objects.create(user=user,
                                                                status=1,
                                                                duration_total='01:00:00',
                                                                price_total=450.00,
                                                                date_from='2019-04-15T16:00:00Z',
                                                                date_to='2019-04-15T17:00:00Z',
                                                                extra_info='',
                                                                )
        appointment_request.services.add(service)
        appointment_request.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)


