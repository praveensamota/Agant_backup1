# Generated by Django 4.2.6 on 2023-10-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agant',
            name='uniprotid',
            field=models.URLField(max_length=100),
        ),
    ]
