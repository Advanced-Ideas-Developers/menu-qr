from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateField(
        auto_now=True, verbose_name='Última actualización')

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'
    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.OneToOneField(to='Restaurant',verbose_name='Restaurante',on_delete=models.CASCADE)
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateField(
        auto_now=True, verbose_name='Última actualización')
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Nombre de Categoría')
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateField(
        auto_now=True, verbose_name='Última actualización')
    def __str__(self):
        return self.name

class MenuDetail(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Menú')
    product_name = models.CharField(max_length=50, verbose_name='Producto')
    description = models.TextField(verbose_name='Descripción')
    price = models.FloatField(verbose_name='Precio')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Categoría')
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateField(
        auto_now=True, verbose_name='Última actualización')
    def __str__(self):
        return self.name
    