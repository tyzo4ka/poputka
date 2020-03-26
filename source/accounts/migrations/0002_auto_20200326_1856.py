# Generated by Django 2.2 on 2020-03-26 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('client', 'Клиент'), ('driver', 'Водитель')], max_length=20, verbose_name='Тип')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None, verbose_name='Мобильный телефон')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('status', models.CharField(blank=True, choices=[('free', 'Свободен'), ('busy', 'Занят')], max_length=20, null=True, verbose_name='Статус')),
                ('car_model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель авто')),
                ('car_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер авто')),
                ('car_seats', models.IntegerField(blank=True, null=True, verbose_name='Количество мест')),
                ('notification', models.BooleanField(default=True, verbose_name='Уведомления')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users_photo', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
