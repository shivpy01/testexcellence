from rest_framework import viewsets

from .models import test_score
from . import serializers

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = test_score.objects.all()
    serializer_class = serializers.CandidateSerializer