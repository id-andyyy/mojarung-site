from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    bio = models.TextField(blank=True, verbose_name='био')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, related_name='members', verbose_name='роль')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'
        ordering = ['time_create']


class Role(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
