# Generated by Django 5.0.1 on 2025-04-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='duration',
            field=models.CharField(choices=[('1_month', '1 Month'), ('3_months', '3 Months'), ('6_months', '6 Months'), ('12_months', '12 Months')], default='1_month', max_length=20),
        ),
    ]
