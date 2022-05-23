# Generated by Django 4.0.4 on 2022-05-02 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_ingredients_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_items',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='date_purchased',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.menu_items'),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meal_price', to='ingredients.menu_items'),
        ),
    ]