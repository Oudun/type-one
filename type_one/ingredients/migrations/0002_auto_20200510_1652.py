# Generated by Django 3.0.5 on 2020-05-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='glycemic_index',
            field=models.IntegerField(null=True),
        ),
    ]
