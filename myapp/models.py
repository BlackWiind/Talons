from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название отделения')

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"

    def __str__(self):
        return self.name


class IdDepartments(models.Model):
    id_value = models.IntegerField(verbose_name='Номер отделения')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отделение')

    class Meta:
        verbose_name = "Номер отделения"
        verbose_name_plural = "Номера отделений"


class Services(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название услуги')
    type = models.CharField(max_length=50, verbose_name='Тип')
    price = models.CharField(max_length=50, verbose_name='Цена')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отделение')

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
