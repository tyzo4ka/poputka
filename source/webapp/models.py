from django.db import models


class Ad(models.Model):
    user = models.ManyToManyField('auth.User', related_name='ad', verbose_name='Автор')
    direction = models.CharField(max_length=50, verbose_name='Направление')
    time = models.DateTimeField(verbose_name='Время выезда')
    seats = models.IntegerField(verbose_name='Количество мест')
    luggage = models.CharField(max_length=100, verbose_name='Багаж')
    place_from = models.CharField(max_length=100, verbose_name='Пункт отправки')
    place_to = models.CharField(max_length=100, verbose_name='Пункт прибытия')
    car_number = models.CharField(max_length=15, verbose_name='Номер авто')
    car = models.CharField(max_length=15, verbose_name='Марка авто')
    price = models.IntegerField(verbose_name='Цена')


class Photo(models.Model):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='photo', verbose_name='Обьявление')
    photo = models.ImageField(upload_to='ads_photo', null=True, blank=True, verbose_name='Фото')





