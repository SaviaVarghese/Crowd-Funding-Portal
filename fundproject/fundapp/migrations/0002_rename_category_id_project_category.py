# Generated by Django 4.2.1 on 2023-05-25 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category_id',
            new_name='category',
        ),
    ]
