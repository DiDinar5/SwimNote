from django.db import models

# Create your models here.
class SexField(models.TextChoices):
    MALE = 'М'
    FEMALE = 'Ж'

class StyleField(models.TextChoices):
    FREESTYLE = 'кроль'
    BUTTERFLY = 'дельфин'
    BACKSTROKE = 'на спине'
    BREASTSTROKE = 'брасс'
    MEDLEY = 'комплекс'

class Athlete(models.Model):
    name = models.CharField(max_length=50)
    extra = models.CharField(max_length=500, null=True)
    birthday = models.DateField()
    sex = models.CharField(max_length=1,
                           choices = SexField.choices,
                           default = SexField.MALE)
    style = models.CharField(max_length=16,
                             choices = StyleField.choices,
                             default = StyleField.FREESTYLE)
class PersonalBest(models.Model):
    style = models.CharField(max_length=16,
                             choices=StyleField.choices,
                             default=StyleField.FREESTYLE)
    time = models.DurationField()
    distance = models.PositiveIntegerField()

