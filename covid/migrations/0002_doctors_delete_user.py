# Generated by Django 5.0.2 on 2024-02-26 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=10)),
                ('dob', models.CharField(default='', max_length=25)),
                ('address', models.CharField(default='', max_length=150)),
                ('emailid', models.CharField(default='', max_length=100)),
                ('mobileno', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('photograph', models.ImageField(upload_to='static/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.city')),
                ('states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='covid.states')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]