# Generated by Django 4.0.4 on 2022-05-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_alter_stock_required_ingredients_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='stock',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='menu_items',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
