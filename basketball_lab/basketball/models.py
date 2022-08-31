from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    division = models.CharField(max_length=100, null=False)
    wins = models.SmallIntegerField()
    losses = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=200, null=False)
    age = models.SmallIntegerField()
    injured = models.CharField(max_length=3, default= 'Enter or Yes/No')
    points = models.FloatField()
    rebounds = models.FloatField()
    assists = models. FloatField()

    def __str__(self):
        return self.lastName
