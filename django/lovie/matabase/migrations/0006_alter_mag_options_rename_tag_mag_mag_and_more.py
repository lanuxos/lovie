# Generated by Django 4.1 on 2022-08-11 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matabase', '0005_rename_tag_mag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mag',
            options={'ordering': ['magReference']},
        ),
        migrations.RenameField(
            model_name='mag',
            old_name='tag',
            new_name='mag',
        ),
        migrations.RenameField(
            model_name='mag',
            old_name='reference',
            new_name='magReference',
        ),
    ]
