# Generated by Django 4.2.4 on 2023-08-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_mailinglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglog',
            name='successful_deliveries',
            field=models.IntegerField(default=0, verbose_name='успешно доставлено'),
        ),
    ]