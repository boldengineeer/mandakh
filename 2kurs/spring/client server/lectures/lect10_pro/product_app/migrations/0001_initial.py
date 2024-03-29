# Generated by Django 5.0.3 on 2024-03-26 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('cdesc', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('pdesc', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.category')),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]
