# Generated by Django 2.2 on 2020-03-23 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None, verbose_name='Мобильный телефон')),
                ('notification', models.BooleanField(verbose_name='Уведомления')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users_photo', verbose_name='Фото')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='accounts.City', verbose_name='Город')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_country', to='accounts.Country', verbose_name='Страна')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('free', 'Свободен'), ('busy', 'Занят')], max_length=20, verbose_name='Статус')),
                ('car', models.CharField(max_length=50, verbose_name='Авто')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='accounts.Profile', verbose_name='Водитель')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='accounts.Country', verbose_name='Страна'),
        ),
    ]