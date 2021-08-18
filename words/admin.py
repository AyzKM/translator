from django.contrib import admin
from .models import Lemma, WordEncounter, WordForms

admin.site.register(Lemma)
admin.site.register(WordEncounter)
admin.site.register(WordForms)
