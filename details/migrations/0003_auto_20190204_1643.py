# Generated by Django 2.1.2 on 2019-02-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20190204_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
