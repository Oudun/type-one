# Generated by Django 3.0.5 on 2020-05-09 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_meal_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='meal',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='records.Record'),
        ),
    ]
