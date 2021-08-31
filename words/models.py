from django.db import models
from django.db.models.fields import TextField
from django.utils import translation
from users.models import User

#from en to kg

class Lemma(models.Model):
    lemma = models.TextField()
    definition = models.TextField()
    frequency_rank = models.IntegerField(null=True, blank=True)
    lang = models.TextField()
    translation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.lemma

class WordForms(models.Model):
    lemma = models.ForeignKey(to=Lemma, on_delete=models.CASCADE, null=True, blank=True)
    form = models.TextField(null=True, blank=True)
    lang = models.TextField(null=True, blank=True) 
    translation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.form

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"

class WordEncounter(models.Model):
    # CONTEXT = [
    #     (1, 'business'),
    #     (2, 'academic'),
    #     (3, 'literary'),
    # ]
    # context = models.IntegerField(choices=CONTEXT, null=True, blank=True)

    encounter = models.IntegerField()
    knowing_status = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, )
    word_form = models.ForeignKey(to=WordForms, on_delete=models.CASCADE, related_name='word_encounter')



