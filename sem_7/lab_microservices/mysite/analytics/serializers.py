from rest_framework import serializers

from sem_7.lab_microservices.mysite.analytics.models import VotingStatistics


class AnalyticsSerializer(serializers.Serializer):
    total_votes = serializers.IntegerField()

class VotingStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingStatistics
        fields = '__all__'