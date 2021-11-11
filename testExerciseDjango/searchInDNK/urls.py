from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('API/', IndexAPIView.as_view(), name='api'),
]