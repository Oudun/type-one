# Generated by Django 3.0.5 on 2020-05-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200501_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='notes',
            field=models.CharField(max_length=32, null=True),
        ),
    ]