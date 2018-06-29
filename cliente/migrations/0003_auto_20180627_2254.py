# Generated by Django 2.0 on 2018-06-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20180626_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segurodetail',
            name='choice_reboque_distancia',
            field=models.CharField(choices=[('7', '7 dias'), ('10', '14 dias')], max_length=2, verbose_name='reboque_distancia'),
        ),
        migrations.AlterField(
            model_name='segurodetail',
            name='choice_reserva',
            field=models.CharField(choices=[('300', '300Km'), ('500', '500Km')], max_length=2, verbose_name='carro_reserva'),
        ),
    ]
