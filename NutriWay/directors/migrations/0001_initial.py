# Generated by Django 5.2 on 2025-04-23 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_alter_certificate_created_at_alter_certificate_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialistRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('feedback', models.TextField(blank=True)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.director')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.specialist')),
            ],
        ),
    ]
