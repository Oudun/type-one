# Generated by Django 3.0.5 on 2020-05-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200501_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='glucose_level',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='insulin_amount',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='notes',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
