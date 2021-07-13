from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100, default="Title")
    numberOfAnswersChoices = [(2, 2), (4,4)]
    numberOfAnswers = models.IntegerField(
       choices=numberOfAnswersChoices,
        default = 4,
    )
    pointsChoices =[(5,5),(10,10),(15,15)]
    points = models.IntegerField(
        choices=pointsChoices,
        default = 5,
    )

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=15)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title