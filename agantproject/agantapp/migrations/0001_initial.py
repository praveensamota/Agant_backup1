# Generated by Django 4.2.6 on 2023-10-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdbid', models.CharField(max_length=200)),
                ('l_id', models.CharField(max_length=100)),
                ('_type', models.CharField(max_length=100)),
                ('uniprotid', models.CharField(max_length=100)),
            ],
        ),
    ]