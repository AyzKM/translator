from words.viewsets import *
from users.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lemma', LemmaListViewSet)
router.register('words', WordFormViewSet)
router.register('user', UserViewSet)
router.register('encounter', WordEncounterViewSet)
