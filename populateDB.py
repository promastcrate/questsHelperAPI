import random
from datetime import time
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "questCityBot.settings")
django.setup()
from django.utils import timezone

from core.models import (
    Quest, Location, QuestLocation, Guide, QuestGuide,
    Participant, Question, Answer, QuestParticipant, Review, TelegramUser, City
)


def populate_db():
    cities = [
        "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
        "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону"
    ]
    for city_name in cities:
        City.objects.create(
            CityName=city_name,
            Country="Россия",
            Population=random.randint(500000, 5000000),
            Description=f"Описание города {city_name}"
        )

    cities = City.objects.all()
    for city in cities:
        for i in range(2):
            Quest.objects.create(
                QuestName=f"Квест в {city.CityName} #{i+1}",
                CityID=city,
                Duration=time(hour=random.randint(1, 3), minute=0),
                Price=random.randint(500, 2000),
                Description=f"Описание квеста в {city.CityName}",
                MaxParticipants=random.randint(5, 15)
            )

    for city in cities:
        for i in range(2):
            Location.objects.create(
                LocationName=f"Локация {i+1} в {city.CityName}",
                CityID=city,
                Address=f"Адрес локации {i+1} в {city.CityName}",
                Description=f"Описание локации {i+1} в {city.CityName}"
            )

    quests = Quest.objects.all()
    locations = Location.objects.all()
    for quest in quests:
        for i, location in enumerate(locations.filter(CityID=quest.CityID)[:3]):
            QuestLocation.objects.create(
                QuestID=quest,
                LocationID=location,
                OrderNumber=i+1
            )

    guides = [
        ("Иван", "Иванов"), ("Петр", "Петров"), ("Анна", "Сидорова"),
        ("Елена", "Смирнова"), ("Дмитрий", "Кузнецов"), ("Ольга", "Васильева"),
        ("Сергей", "Михайлов"), ("Мария", "Федорова"), ("Алексей", "Соколов"),
        ("Наталья", "Попова")
    ]
    for first_name, last_name in guides:
        Guide.objects.create(
            FirstName=first_name,
            LastName=last_name,
            Phone=f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}",
            Email=f"{first_name.lower()}.{last_name.lower()}@example.com",
            Experience=random.randint(1, 10)
        )

    guides = Guide.objects.all()
    for quest in quests:
        for guide in random.sample(list(guides), 2):
            QuestGuide.objects.create(
                QuestID=quest,
                GuideID=guide
            )

    participants = [
        ("Алексей", "Смирнов"), ("Екатерина", "Иванова"), ("Дмитрий", "Петров"),
        ("Ольга", "Кузнецова"), ("Сергей", "Васильев"), ("Наталья", "Михайлова"),
        ("Иван", "Федоров"), ("Мария", "Соколова"), ("Андрей", "Попов"),
        ("Татьяна", "Николаева")
    ]
    for first_name, last_name in participants:
        Participant.objects.create(
            FirstName=first_name,
            LastName=last_name,
            TelegramUserID=random.randint(100000000, 999999999)
        )

    participants = Participant.objects.all()
    for participant in participants:
        for i in range(2):
            Question.objects.create(
                ParticipantID=participant,
                QuestionText=f"Вопрос {i+1} от {participant.FirstName} {participant.LastName}",
                IsAnswered=random.choice([True, False])
            )

    questions = Question.objects.filter(IsAnswered=True)
    for question in questions:
        Answer.objects.create(
            QuestionID=question,
            AnswerText=f"Ответ на вопрос {question.QuestionText}"
        )

    quests = Quest.objects.all()
    participants = Participant.objects.all()
    for quest in quests:
        for participant in random.sample(list(participants), 3):
            QuestParticipant.objects.create(
                QuestID=quest,
                ParticipantID=participant
            )

    for quest in quests:
        for participant in random.sample(list(participants), 2):
            Review.objects.create(
                QuestID=quest,
                ParticipantID=participant,
                Rating=random.randint(1, 5),
                Comment=f"Отзыв на квест {quest.QuestName} от {participant.FirstName} {participant.LastName}"
            )

    telegram_users = [
        (123456789, "Иван", "Иванов", "ivan_ivanov", "ru"),
        (987654321, "Петр", "Петров", "petr_petrov", "en"),
        (111111111, "Анна", "Сидорова", "anna_sidorova", "ru"),
        (222222222, "Елена", "Смирнова", "elena_smirnova", "en"),
        (333333333, "Дмитрий", "Кузнецов", "dmitry_kuznetsov", "ru"),
        (444444444, "Ольга", "Васильева", "olga_vasileva", "en"),
        (555555555, "Сергей", "Михайлов", "sergey_mikhailov", "ru"),
        (666666666, "Мария", "Федорова", "maria_fedorova", "en"),
        (777777777, "Алексей", "Соколов", "alexey_sokolov", "ru"),
        (888888888, "Наталья", "Попова", "natalia_popova", "en")
    ]
    for user_id, first_name, last_name, username, language_code in telegram_users:
        TelegramUser.objects.create(
            UserID=user_id,
            FirstName=first_name,
            LastName=last_name,
            Username=username,
            LanguageCode=language_code
        )

    print("База данных успешно заполнена тестовыми данными.")


if __name__ == "__main__":
    populate_db()