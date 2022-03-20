# Generated by Django 3.2.12 on 2022-02-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.TextField(max_length=150)),
                ('Image', models.ImageField(upload_to='IMG')),
                ('Book_description', models.TextField(max_length=350)),
            ],
        ),
    ]