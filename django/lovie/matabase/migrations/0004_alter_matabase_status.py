# Generated by Django 4.1 on 2022-08-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matabase', '0003_alter_matabase_title_alter_matabase_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matabase',
            name='status',
            field=models.CharField(choices=[('d', 'Downloaded'), ('w', 'Watched'), ('r', 'Removed')], default='d', help_text='d: Downloaded, w: Watched, r: Removed', max_length=10),
        ),
    ]
