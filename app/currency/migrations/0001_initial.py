# Generated by Django 4.0.2 on 2022-02-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.CharField(max_length=64)),
                ('subject', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]