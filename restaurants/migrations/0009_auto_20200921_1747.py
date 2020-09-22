# Generated by Django 3.1.1 on 2020-09-21 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurant_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Producto')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.menu', verbose_name='Menú'),
        ),
        migrations.DeleteModel(
            name='MenuDetail',
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.category', verbose_name='Category'),
        ),
    ]
