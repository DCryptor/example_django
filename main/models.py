from django.db import models

# Create your models here.


class UserProfile (models.Model):
    second_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    class_name = models.CharField('Кружок', max_length=50)

    def __str__(self):
        return self.second_name

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
