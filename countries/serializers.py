from rest_framework import serializers
from countries.models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["id", "countrie", "liked", "created_at",]