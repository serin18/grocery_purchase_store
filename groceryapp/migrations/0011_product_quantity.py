# Generated by Django 4.1.5 on 2024-05-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0010_deliveryprofiletable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
