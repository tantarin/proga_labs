from rest_framework import serializers

class AnalyticsSerializer(serializers.Serializer):
    total_votes = serializers.IntegerField()