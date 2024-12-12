# Generated by Django 5.1.2 on 2024-12-12 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_orderhistorty_cart_remove_cartitem_cart_and_more'),
        ('autoparts', '0003_alter_product_part_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profilecustomer')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSellersHistorty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.profilecustomer')),
                ('sellers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profileseller', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistorty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profilecustomer')),
                ('sellers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profileseller')),
            ],
        ),
    ]
