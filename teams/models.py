from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
