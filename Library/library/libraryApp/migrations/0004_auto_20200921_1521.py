# Generated by Django 3.0.7 on 2020-09-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0003_auto_20200921_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lib',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
