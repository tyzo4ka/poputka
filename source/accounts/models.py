from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

DRIVER_STATUS_CHOICES = (
    ('free', 'Свободен'),
    ('busy', 'Занят'),
)

class Profile(models.Model):
    user = models.ForeignKey('auth.User', related_name='profile', on_delete=models.CASCADE, verbose_name='пользователь')
    mobile_phone = PhoneNumberField(max_length=20, verbose_name='Мобильный телефон')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='profile_country', verbose_name='Страна')
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='city', verbose_name='Город')
    notification = models.BooleanField(verbose_name='Уведомления')
    photo = models.ImageField(upload_to='users_photo', null=True, blank=True, verbose_name='Фото')


class Driver(models.Model):
    profile = models.ForeignKey('Profile', related_name='driver', on_delete=models.CASCADE, verbose_name='Водитель')
    status = models.CharField(max_length=20, choices=DRIVER_STATUS_CHOICES, verbose_name='Статус')
    car = models.CharField(max_length=50, verbose_name='Авто')


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Страна')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Город')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country', verbose_name='Страна',
                            default=None)

    def __str__(self):
        return self.name
