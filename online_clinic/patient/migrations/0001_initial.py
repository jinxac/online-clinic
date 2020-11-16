# Generated by Django 3.1.3 on 2020-11-16 10:50

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import djchoices.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0003_employeerole_indepartment_role_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(choices=[('CR', 'Created'), ('IP', 'InProgress'), ('PO', 'Postpone'), ('CA', 'Cancelled')], max_length=2, validators=[djchoices.choices.ChoicesValidator({'CA': 'Cancelled', 'CR': 'Created', 'IP': 'InProgress', 'PO': 'Postpone'})])),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PatientCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('in_progress', models.BooleanField(default=True)),
                ('total_cost', models.DecimalField(decimal_places=6, default=Decimal('0.000000'), max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=6, default=Decimal('0.000000'), max_digits=10)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.appointmentstatus')),
                ('in_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.department')),
                ('patient_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientcase')),
            ],
        ),
    ]
