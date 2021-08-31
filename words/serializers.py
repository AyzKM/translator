from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from .models import Lemma, WordForms, WordEncounter

User = get_user_model()

class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = '__all__'

class WordEncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordEncounter
        fields = '__all__'

class WordFormsSerializer(serializers.ModelSerializer):

    word_encounter = WordEncounterSerializer(many=True, read_only=True)

    class Meta:
        model = WordForms
        fields = ['form', 'translation', 'word_encounter']