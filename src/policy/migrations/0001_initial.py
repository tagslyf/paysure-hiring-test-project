# Generated by Django 3.0.3 on 2020-02-19 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_user_id', models.CharField(max_length=255, unique=True)),
                ('benefit', models.CharField(choices=[('dentist', 'Dentist'), ('optician', 'Optician'), ('gynecologist', 'Gynecologist')], max_length=255)),
                ('currency', models.CharField(choices=[('usd', 'USD'), ('gbp', 'GBP'), ('php', 'PHP')], max_length=3)),
                ('total_max_amount', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'policy_policy',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.Policy')),
            ],
            options={
                'db_table': 'policy_payment',
            },
        ),
    ]
