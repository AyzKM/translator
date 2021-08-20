from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LemmaListAPIView.as_view(), name='words'),
    path('form', WordFormsListCreateAPIView.as_view(), name='form'),
    path('sentence', InputSentenceCreateAPIVew.as_view(), name='sentence')

    # path('<int:pk>/', )
]

# urlpatterns = [
#     path('', UserListCreateAPIView.as_view(), name='users'),
#     path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
#     path('api-auth', include('rest_framework.urls')),
#     # path('auth/', include('djoser.urls')),
#     path('registr/', RegistrationAPIView.as_view(), name='register')
# ]