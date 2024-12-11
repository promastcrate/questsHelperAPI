from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    CityViewSet, QuestViewSet, LocationViewSet, QuestLocationViewSet,
    GuideViewSet, QuestGuideViewSet, ParticipantViewSet, QuestParticipantViewSet,
    ReviewViewSet, ParticipantView, QuestionViewSet, AnswerViewSet
)

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'quests', QuestViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'quest-locations', QuestLocationViewSet)
router.register(r'guides', GuideViewSet)
router.register(r'quest-guides', QuestGuideViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'quest-participants', QuestParticipantViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('participants/', ParticipantView.as_view(), name='participant-create-update'),
]
