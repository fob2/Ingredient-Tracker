# Generated by Django 4.0.4 on 2022-05-25 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0005_ingredients_price_ingredients_stock_menu_items_price'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock_required',
            unique_together={('menu_items', 'ingredients')},
        ),
    ]