from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def test_email(request):
    try:
        send_mail(
            subject='Тестовое письмо',
            message='Это тестовое письмо из Django',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['kinst@inbox.ru'],  # укажите свой email для теста
        )
        return HttpResponse('Письмо отправлено успешно!')
    except Exception as e:
        return HttpResponse(f'Ошибка: {e}')