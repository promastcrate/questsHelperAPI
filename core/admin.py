from django.contrib import admin
from .models import City, Quest, Location, QuestLocation, Guide, QuestGuide, Participant, QuestParticipant, Review, \
    Question, Answer

admin.site.register(City)
admin.site.register(Quest)
admin.site.register(Location)
admin.site.register(QuestLocation)
admin.site.register(Guide)
admin.site.register(QuestGuide)
admin.site.register(Participant)
admin.site.register(QuestParticipant)
admin.site.register(Review)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('ParticipantID', 'QuestionText', 'QuestionDate', 'IsAnswered')
    list_filter = ('IsAnswered', 'QuestionDate')
    search_fields = ('ParticipantID__FirstName', 'ParticipantID__LastName', 'QuestionText')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('QuestionID', 'AnswerText', 'AnswerDate')
    list_filter = ('AnswerDate',)
    search_fields = ('QuestionID__QuestionText', 'AnswerText')