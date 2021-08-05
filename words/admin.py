from django.contrib import admin
from .models import Lemma, WordEncounter, Forms

admin.site.register(Lemma)
admin.site.register(WordEncounter)
admin.site.register(Forms)
