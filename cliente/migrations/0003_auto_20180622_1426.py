# Generated by Django 2.0 on 2018-06-22 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20180622_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fipedetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='fipedetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cliente.Cliente'),
        ),
    ]