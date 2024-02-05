from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    url = models.CharField(max_length=100, verbose_name='ссылка')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Меню'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Меню'  # Настройка для наименования набора объектов
        ordering = ('name',)


