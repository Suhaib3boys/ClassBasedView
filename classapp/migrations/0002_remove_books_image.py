# Generated by Django 3.2.12 on 2022-02-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='Image',
        ),
    ]