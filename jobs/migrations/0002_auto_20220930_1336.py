# Generated by Django 3.2.5 on 2022-09-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
