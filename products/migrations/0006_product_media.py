# Generated by Django 3.1.2 on 2020-10-29 09:33

from django.db import migrations, models
import django.utils.timezone
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(default=django.utils.timezone.now, storage=products.storages.ProtectedStorage, upload_to='products/'),
            preserve_default=False,
        ),
    ]
