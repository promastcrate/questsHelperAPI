from django.db import models

# Таблица Города
class City(models.Model):
    CityID = models.AutoField(primary_key=True)
    CityName = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Population = models.IntegerField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.CityName

# Таблица Квесты
class Quest(models.Model):
    QuestID = models.AutoField(primary_key=True)
    QuestName = models.CharField(max_length=200)
    CityID = models.ForeignKey(City, on_delete=models.CASCADE)
    Duration = models.TimeField()
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    Description = models.TextField()
    MaxParticipants = models.IntegerField()

    def __str__(self):
        return self.QuestName

class Location(models.Model):
    LocationID = models.AutoField(primary_key=True)
    LocationName = models.CharField(max_length=200)
    CityID = models.ForeignKey(City, on_delete=models.CASCADE)
    Address = models.CharField(max_length=255)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.LocationName

class QuestLocation(models.Model):
    QuestID = models.ForeignKey(Quest, on_delete=models.CASCADE)
    LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    OrderNumber = models.IntegerField()

    class Meta:
        unique_together = ('QuestID', 'LocationID')

    def __str__(self):
        return f"{self.QuestID.QuestName} - {self.LocationID.LocationName}"

class Guide(models.Model):
    GuideID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()
    Experience = models.IntegerField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class QuestGuide(models.Model):
    QuestID = models.ForeignKey(Quest, on_delete=models.CASCADE)
    GuideID = models.ForeignKey(Guide, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('QuestID', 'GuideID')

    def __str__(self):
        return f"{self.QuestID.QuestName} - {self.GuideID.FirstName} {self.GuideID.LastName}"

class Participant(models.Model):
    ParticipantID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    TelegramUserID = models.BigIntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Question(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    ParticipantID = models.ForeignKey(Participant, on_delete=models.CASCADE)
    QuestionText = models.TextField()
    QuestionDate = models.DateTimeField(auto_now_add=True)
    IsAnswered = models.BooleanField(default=False)

    def __str__(self):
        return f"Вопрос от {self.ParticipantID} ({self.QuestionDate})"

class Answer(models.Model):
    AnswerID = models.AutoField(primary_key=True)
    QuestionID = models.OneToOneField(Question, on_delete=models.CASCADE)
    AnswerText = models.TextField()
    AnswerDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ответ на вопрос {self.QuestionID} ({self.AnswerDate})"

class QuestParticipant(models.Model):
    QuestID = models.ForeignKey(Quest, on_delete=models.CASCADE)
    ParticipantID = models.ForeignKey(Participant, on_delete=models.CASCADE)
    RegistrationDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('QuestID', 'ParticipantID')

    def __str__(self):
        return f"{self.QuestID.QuestName} - {self.ParticipantID.FirstName} {self.ParticipantID.LastName}"

class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    QuestID = models.ForeignKey(Quest, on_delete=models.CASCADE)
    ParticipantID = models.ForeignKey(Participant, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Comment = models.TextField()
    ReviewDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.QuestID.QuestName} - {self.ParticipantID.FirstName} {self.ParticipantID.LastName}"


class TelegramUser(models.Model):
    UserID = models.BigIntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    LanguageCode = models.CharField(max_length=10, null=True, blank=True)
    RegistrationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} (@{self.Username})"