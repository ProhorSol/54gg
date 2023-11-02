from django.db import models

class Staff(models.Model):
    name = models.CharField('Имя', max_length=70)
    number = models.CharField('Номер', max_length=500)
    mail = models.EmailField('Почта')
    ph_number = models.CharField('Номер телефона', max_length=50)
    jobs = (
        ('Программист', 'Программист'),
        ('Инженер', 'Инженер'),
        ('Оператор', 'Оператор')
    )
    jb = models.CharField('Должность', max_length=100, choices=jobs, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'



