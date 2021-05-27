from rest_framework import serializers
from .models import test_score

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_score
        fields = '__all__'