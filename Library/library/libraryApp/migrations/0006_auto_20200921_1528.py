# Generated by Django 3.0.7 on 2020-09-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0005_auto_20200921_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lib',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
