# Generated by Django 4.2.6 on 2023-11-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('number', models.CharField(max_length=500, verbose_name='Номер')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта')),
                ('ph_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('jb', models.CharField(choices=[('Программист', 'Программист'), ('Инженер', 'Инженер'), ('Оператор', 'Оператор')], default='', max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]
