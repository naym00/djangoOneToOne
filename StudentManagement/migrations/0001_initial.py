# Generated by Django 3.1.3 on 2021-08-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=5)),
                ('phoneNumber', models.CharField(max_length=15)),
            ],
        ),
    ]
