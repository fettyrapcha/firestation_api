# Generated by Django 4.0 on 2021-12-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('img', models.ImageField(blank='True', null='True', upload_to='upload_path')),
                ('massage', models.TextField(max_length=350)),
            ],
        ),
    ]
