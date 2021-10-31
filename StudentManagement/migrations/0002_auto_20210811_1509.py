# Generated by Django 3.1.3 on 2021-08-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MLE', 'MALE'), ('FML', 'FEMALE')], default='MLE', max_length=3),
        ),
    ]