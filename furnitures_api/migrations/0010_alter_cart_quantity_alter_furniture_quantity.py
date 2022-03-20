# Generated by Django 4.0.3 on 2022-03-20 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures_api', '0009_alter_furniture_orderquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='furnitures_api.furniture', to_field='quantity'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='quantity',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]