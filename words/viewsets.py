from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Lemma, WordForms
from .serializers import *

class LemmaListViewSet(viewsets.ModelViewSet):
    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer

class WordFormViewSet(viewsets.ModelViewSet):
    serializer_class = WordFormsSerializer
    queryset = WordForms.objects.all()

    def create(self, request):
        data = request.POST
        serializer = WordFormsSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.validated_data.get('sentence')
            lst_words = ''.join(obj).split()
            word_dict = {}
            for word in lst_words:
                if self.queryset.filter(form__icontains=word):
                    word_dict[f'{self.queryset.filter(form__icontains=word)}'] = self.queryset.filter(form__icontains=word).values_list('translation')
                else:
                    self.queryset.create(form=word, sentence=obj)
            return Response(data=word_dict) 
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

