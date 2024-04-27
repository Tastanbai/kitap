# Generated by Django 5.0.3 on 2024-04-24 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_returnedbook'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='returnedbook',
            name='city',
            field=models.CharField(max_length=32, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='date_in',
            field=models.DateField(blank=True, null=True, verbose_name='Дата возврата'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='date_out',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='iin',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ИИН'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='name',
            field=models.CharField(max_length=32, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='returnedbook',
            name='quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='returnedbook',
            name='additional_info',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='returnedbook',
            name='book_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='returnedbook',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='returnedbook',
            name='return_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата возврата книги'),
        ),
        migrations.AlterField(
            model_name='returnedbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]