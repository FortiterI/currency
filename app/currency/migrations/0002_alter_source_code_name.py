# Generated by Django 4.0.2 on 2022-05-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='code_name',
            field=models.PositiveIntegerField(choices=[(1, 'PrivatBank'), (2, 'MonoBank'), (3, 'vkurse.')], unique=True),
        ),
    ]
