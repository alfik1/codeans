from api.models import Questions,Answers
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model =User
        fields=['username','email','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class QuestionSerializer(serializers.ModelSerializer):

    user=serializers.CharField(read_only=True)
    create_date=serializers.CharField(read_only=True)
    class Meta:
        model=Questions
        fields='__all__'

class AnswerSerializer(serializers.ModelSerializer):
    questions=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    upvotes=serializers.CharField(read_only=True)
    posted_date=serializers.CharField(read_only=True)
    class Meta:
        model =Answers
        fields='__all__'