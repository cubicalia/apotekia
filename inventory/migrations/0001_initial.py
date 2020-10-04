# Generated by Django 3.1.1 on 2020-09-28 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0005_auto_20200921_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Location name')),
            ],
            options={
                'verbose_name': 'Inventory Location',
                'verbose_name_plural': 'Inventory Locations',
            },
        ),
        migrations.CreateModel(
            name='InventoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date and time of entries')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.inventorylocation')),
            ],
            options={
                'verbose_name': 'Inventory Table',
                'verbose_name_plural': 'Inventory Tables',
            },
        ),
        migrations.CreateModel(
            name='InventoryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1, verbose_name='Initial count')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.inventorylocation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Inventory Entry',
                'verbose_name_plural': 'Inventory Entries',
            },
        ),
    ]
