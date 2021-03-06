# Generated by Django 3.0.5 on 2020-05-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '__first__'),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Ingredient')),
                ('ingredient_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.IngredientUnit')),
                ('record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Record')),
            ],
        ),
    ]
