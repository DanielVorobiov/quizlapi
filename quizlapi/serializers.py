from rest_framework import serializers
from .models import Question, Answer, Game
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        user = UserModel.objects.create_user(
            username=validate_data['username'],
            password=validate_data['password']
        )
        return user

    class Meta:
        model = UserModel
        fields = ("id")



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'numberOfAnswers', 'points')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('title', 'correct',)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('title',)


