# Generated by Django 5.0.6 on 2024-11-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_news_user_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returnedbook',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта'),
        ),
    ]