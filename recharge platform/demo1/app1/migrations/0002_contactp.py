# Generated by Django 4.1.2 on 2022-12-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=100)),
            ],
        ),
    ]