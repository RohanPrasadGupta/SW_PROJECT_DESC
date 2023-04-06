# Generated by Django 4.0.3 on 2023-04-04 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('device_id', models.CharField(max_length=4)),
                ('phone', models.PositiveIntegerField()),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('on_site', models.BooleanField(default=False)),
                ('case_type', models.SmallIntegerField()),
                ('case_status', models.BooleanField(default=False)),
                ('note', models.CharField(default='', max_length=100)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction_mng.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('check_in', models.TimeField(auto_now_add=True)),
                ('check_out', models.TimeField(auto_now=True)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction_mng.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('on_site', models.BooleanField(default=False)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction_mng.worker')),
            ],
        ),
    ]
