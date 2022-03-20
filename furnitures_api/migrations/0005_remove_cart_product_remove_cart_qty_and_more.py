# Generated by Django 4.0.3 on 2022-03-20 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('furnitures_api', '0004_cart_user_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.CharField(default='NA', max_length=32),
        ),
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AddField(
            model_name='cart',
            name='imgURL',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default='NA', max_length=32),
        ),
        migrations.AddField(
            model_name='cart',
            name='orderQuantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='furniture',
            name='orderQuantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='furniture',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(),
        ),
    ]