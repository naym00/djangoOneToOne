# Generated by Django 3.1.3 on 2021-08-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManagement', '0002_auto_20210811_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
