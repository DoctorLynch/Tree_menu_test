from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', **NULLABLE, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Меню'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Меню'  # Настройка для наименования набора объектов


