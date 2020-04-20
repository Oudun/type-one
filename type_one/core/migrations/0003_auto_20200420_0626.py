# Generated by Django 3.0.5 on 2020-04-20 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200417_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='unit',
            name='code',
        ),
        migrations.AddField(
            model_name='ingredientunit',
            name='gramsInUnit',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredientunit',
            name='unit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Unit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('notes', models.CharField(max_length=1000)),
                ('activityPeriod', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.ActivityPeriod')),
                ('insulinShot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.InsulinShot')),
                ('sugarLevel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SugarLevel')),
            ],
        ),
        migrations.CreateModel(
            name='MealIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientWeightGrams', models.IntegerField()),
                ('indredientUnitId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.IngredientUnit')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('glycemicIndex', models.IntegerField()),
                ('breadUnitsPer100g', models.FloatField()),
                ('fatPer100g', models.IntegerField()),
                ('carbohydratePer100g', models.IntegerField()),
                ('proteinPer100g', models.IntegerField()),
                ('energyKkalPer100g', models.IntegerField()),
                ('ingredientType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='ingredientunit',
            name='ingredient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Ingredient'),
            preserve_default=False,
        ),
    ]
