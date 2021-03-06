# Generated by Django 3.2.4 on 2021-07-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliveredAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/sample.jpg', null=True, upload_to=''),
        ),
    ]
