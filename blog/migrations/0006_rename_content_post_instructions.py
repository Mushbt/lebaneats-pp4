# Generated by Django 3.2.21 on 2023-10-04 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='instructions',
        ),
    ]
