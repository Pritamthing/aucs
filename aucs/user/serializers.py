from rest_framework import serializers
from .models import CleanupReport, User

class CleanupReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanupReport
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
