# Generated by Django 4.0.5 on 2022-08-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_person_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profilepic',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]