# Generated by Django 2.1.5 on 2019-02-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190124_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextended',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserExtended',
        ),
    ]
