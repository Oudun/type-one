# Generated by Django 3.0.5 on 2020-04-17 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityCode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SugarLevelUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='insulinshot',
            name='time',
        ),
        migrations.CreateModel(
            name='SugarLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('sugarUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SugarLevelUnit')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Activity')),
            ],
        ),
    ]