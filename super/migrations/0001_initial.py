# Generated by Django 4.0.5 on 2022-10-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('gender', models.TextField(choices=[('male', 'male'), ('female', 'female')])),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('prize', models.IntegerField(max_length=10)),
                ('desc', models.TextField(max_length=10)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
