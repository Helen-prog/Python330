# Generated by Django 5.0.1 on 2024-04-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'товар в корзине', 'verbose_name_plural': 'Корзина'},
        ),
    ]