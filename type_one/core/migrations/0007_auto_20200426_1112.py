# Generated by Django 3.0.5 on 2020-04-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200424_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityperiod',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='activityperiod',
            old_name='startTime',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='breadUnitsPer100g',
            new_name='bread_units_per_100g',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='carbohydratePer100g',
            new_name='carbohydrate_per_100g',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='energyKkalPer100g',
            new_name='energy_kKkal_per_100g',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='fatPer100g',
            new_name='fat_per_100g',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='glycemicIndex',
            new_name='glycemic_index',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='proteinPer100g',
            new_name='protein_per_100g',
        ),
        migrations.RenameField(
            model_name='ingredientunit',
            old_name='gramsInUnit',
            new_name='grams_int_unit',
        ),
        migrations.RenameField(
            model_name='mealingredient',
            old_name='indredientUnitId',
            new_name='indredient_unit',
        ),
        migrations.RenameField(
            model_name='mealingredient',
            old_name='ingredientWeightGrams',
            new_name='ingredient_weight_grams',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='activityPeriod',
            new_name='activity_period',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='insulinShot',
            new_name='insulin_shot',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='sugarLevel',
            new_name='sugar_level',
        ),
        migrations.RenameField(
            model_name='sugarlevel',
            old_name='sugarUnit',
            new_name='sugar_unit',
        ),
        migrations.AddField(
            model_name='mealingredient',
            name='ingredient_units',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
