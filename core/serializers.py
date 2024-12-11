from rest_framework import serializers
from .models import (
    City, Quest, Location, QuestLocation, Guide, QuestGuide, Participant, QuestParticipant, Review, Question, Answer
)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class QuestLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestLocation
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class QuestGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestGuide
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['ParticipantID', 'FirstName', 'LastName','TelegramUserID']

class QuestParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestParticipant
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'