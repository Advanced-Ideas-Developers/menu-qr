# Generated by Django 3.1.1 on 2020-12-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0020_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='clasification',
            field=models.CharField(default='Restaurante', max_length=50),
        ),
    ]