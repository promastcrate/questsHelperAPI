from django.db.models.signals import post_save
from django.dispatch import receiver
import requests

from core.models import Answer


def send_telegram_message(chat_id, text):
    bot_token = "7632300710:AAGvacoXCgWK9XT0jjowXQ--F_IaPT_jvHw"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()

@receiver(post_save, sender=Answer)
def send_answer_notification(sender, instance, created, **kwargs):
    if created:
        question = instance.QuestionID
        participant = question.ParticipantID
        telegram_user_id = participant.TelegramUserID

        if telegram_user_id:
            answer_text = instance.AnswerText
            message_text = f"Вам ответили на вопрос:\n\n{answer_text}"
            send_telegram_message(telegram_user_id, message_text)