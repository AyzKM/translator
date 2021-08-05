from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User

class Rules(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField()
    link = models.CharField(max_length=250)
    lang = models.TextField()
    frequency_rank = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'

    def __str__(self):
        return self.description

class GrammarEncounter(models.Model):
    SECTIONS = [
        (1, 'syntax'),
        (2, 'spelling'),
        (3, 'stylistics'),
    ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='grammar_encounter')
    section = models.IntegerField(choices=SECTIONS)
    rule = models.ForeignKey(to=Rules, on_delete=CASCADE)

    # def __str__(self):
    #     return self.rule


