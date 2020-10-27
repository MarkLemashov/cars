# Generated by Django 2.2.15 on 2020-10-24 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cars',
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Customer'),
        ),
    ]