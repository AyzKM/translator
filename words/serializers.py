from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Lemma, WordForms

User = get_user_model()

class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = '__all__'

class WordFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordForms
        fields = '__all__'


