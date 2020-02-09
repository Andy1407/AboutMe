# Generated by Django 2.2.7 on 2019-11-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutaway', '0003_auto_20191130_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='myexperience',
            name='dark_theme',
            field=models.BooleanField(default='False', max_length=200, verbose_name='Темная тема'),
        ),
        migrations.AlterField(
            model_name='myexperience',
            name='background',
            field=models.ImageField(default='static/image/background_light.jpg', max_length=200, upload_to='image', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='myexperience',
            name='my_photo',
            field=models.ImageField(default='my_photo.jpg', max_length=200, upload_to='image', verbose_name='Моё фото'),
        ),
    ]