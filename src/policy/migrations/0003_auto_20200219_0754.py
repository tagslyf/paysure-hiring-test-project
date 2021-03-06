# Generated by Django 3.0.3 on 2020-02-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_auto_20200219_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='policy',
            name='benefit',
            field=models.CharField(choices=[('dentist', 'Dentist'), ('optician', 'Optician'), ('gynecologist', 'Gynecologist'), ('maintenance', 'Maintenance')], max_length=255),
        ),
        migrations.AlterField(
            model_name='policy',
            name='currency',
            field=models.CharField(choices=[('GBP', 'British Pound'), ('PHP', 'Philippine Peso')], max_length=3),
        ),
    ]
