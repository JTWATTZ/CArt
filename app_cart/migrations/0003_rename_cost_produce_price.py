# Generated by Django 4.1.3 on 2022-11-17 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0002_cart_produce_delete_blog_cart_produce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produce',
            old_name='cost',
            new_name='price',
        ),
    ]
