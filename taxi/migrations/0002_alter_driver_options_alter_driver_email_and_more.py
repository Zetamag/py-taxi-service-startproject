# Generated by Django 4.1.5 on 2023-01-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
