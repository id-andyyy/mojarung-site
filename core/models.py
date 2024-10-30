from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    # image = models.ImageField(upload_to='members/')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, related_name='members')
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['time_created']


class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
