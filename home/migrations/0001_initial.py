# Generated by Django 4.1.7 on 2023-04-07 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('no_notes', models.CharField(max_length=15)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('kasir', 'kasir'), ('owner', 'owner'), ('pemilik', 'pemilik')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('no_notes', models.CharField(max_length=15)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSell',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sell_price', models.FloatField()),
                ('amount_sell', models.IntegerField()),
                ('sub_total_sell', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sell')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='DetailPurchase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('expired_date', models.BigIntegerField()),
                ('purchase_price', models.FloatField()),
                ('amount_buy', models.IntegerField()),
                ('sub_total_buy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percent_buying_margin', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.purchase')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.medicine')),
            ],
        ),
    ]