from django.db.models import query
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lemma, WordForms
from .serializers import *

class LemmaListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lemmas = Lemma.objects.all()
        serializer = LemmaSerializer(lemmas, many=True)
        return Response(data=serializer.data)

class WordFormsListCreateAPIView(ListCreateAPIView):
    serializer_class = WordFormsSerializer
    queryset = WordForms.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = WordFormsSerializer(data=data)
        if serializer.is_valid():
            if self.queryset.filter(form__icontains=data['form']):
                obj = self.queryset.filter(form__icontains=data['form'])
                return Response(data={'message': f'это слова есть в бд: {obj[0]}'})
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


