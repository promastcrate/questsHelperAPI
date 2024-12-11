from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    City, Quest, Location, QuestLocation, Guide, QuestGuide, Participant, QuestParticipant, Review, Question, Answer
)
from .serializers import (
    CitySerializer, QuestSerializer, LocationSerializer, QuestLocationSerializer,
    GuideSerializer, QuestGuideSerializer, ParticipantSerializer, QuestParticipantSerializer,
    ReviewSerializer, QuestionSerializer, AnswerSerializer
)

# ViewSet для Городов
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['CityName', 'Country', 'Population']
    search_fields = ['CityName', 'Country']
    ordering_fields = ['CityName', 'Population']
    ordering = ['CityName']


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['QuestName', 'CityID', 'Duration', 'Price', 'MaxParticipants']
    search_fields = ['QuestName', 'CityID__CityName']  # Поиск по полям
    ordering_fields = ['QuestName', 'Price', 'Duration']
    ordering = ['QuestName']

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['LocationName', 'CityID', 'Address']
    search_fields = ['LocationName', 'Address']
    ordering_fields = ['LocationName']
    ordering = ['LocationName']

class QuestLocationViewSet(viewsets.ModelViewSet):
    queryset = QuestLocation.objects.all()
    serializer_class = QuestLocationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['QuestID', 'LocationID', 'OrderNumber']
    ordering_fields = ['OrderNumber']
    ordering = ['OrderNumber']

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['FirstName', 'LastName', 'Experience']
    search_fields = ['FirstName', 'LastName']
    ordering_fields = ['FirstName', 'Experience']
    ordering = ['FirstName']

class QuestGuideViewSet(viewsets.ModelViewSet):
    queryset = QuestGuide.objects.all()
    serializer_class = QuestGuideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['QuestID', 'GuideID']

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['FirstName', 'LastName', 'TelegramUserID']
    search_fields = ['FirstName', 'LastName']
    ordering_fields = ['FirstName', 'LastName']
    ordering = ['FirstName']

    @action(detail=False, methods=['get'], url_path='by-telegram-id/(?P<telegram_user_id>\d+)')
    def retrieve_by_telegram_id(self, request, telegram_user_id=None):
        try:
            participant = self.get_queryset().get(TelegramUserID=telegram_user_id)
            serializer = self.get_serializer(participant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Participant.DoesNotExist:
            return Response({"error": "Участник с таким TelegramUserID не найден."}, status=status.HTTP_404_NOT_FOUND)

class ParticipantView(APIView):
    def post(self, request, format=None):
        telegram_user_id = request.data.get('TelegramUserID')
        first_name = request.data.get('FirstName')
        last_name = request.data.get('LastName')

        participant = Participant.objects.filter(TelegramUserID=telegram_user_id).first()

        if participant:
            participant.FirstName = first_name
            participant.LastName = last_name
            participant.save()
            return Response({"message": "Участник обновлен", "data": ParticipantSerializer(participant).data}, status=status.HTTP_200_OK)
        else:
            participant_data = {
                "FirstName": first_name,
                "LastName": last_name,
                "TelegramUserID": telegram_user_id
            }
            serializer = ParticipantSerializer(data=participant_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Участник создан", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestParticipantViewSet(viewsets.ModelViewSet):
    queryset = QuestParticipant.objects.all()
    serializer_class = QuestParticipantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['QuestID', 'ParticipantID']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['QuestID', 'ParticipantID', 'Rating']
    search_fields = ['Comment']  # Поиск по тексту комментария
    ordering_fields = ['Rating', 'ReviewDate']
    ordering = ['ReviewDate']




class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer