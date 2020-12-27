from django.db import models


# Create your models here.


class Customer(models.Model):
    """
    модель клиента
    Предназначена для создания в базе данных
    https://docs.djangoproject.com/en/3.0/topics/db/models/
    """
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Номер телефон', unique=True, max_length=15)
    count_children = models.IntegerField('Количество детей')
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.email # возврат значения для админки и отладки

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
