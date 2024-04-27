# Generated by Django 5.0.3 on 2024-04-10 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='balance_quantity',
            field=models.IntegerField(verbose_name='Остаток книг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='ФИО')),
                ('city', models.CharField(max_length=32, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book', verbose_name='Книга')),
            ],
        ),
    ]