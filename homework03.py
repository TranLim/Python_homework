from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import path
from urllib.parse import urlparse
import string
import random

# Задание 3. URL shortener



# Конфигурация, не нужно редактировать
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )

allow = {'http', 'https', 'ftp'}


def random_key():
    """
    Генератор
    """
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(5))


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        context = {}
        url = request.POST.get('url')
        result = urlparse(url)
        if result.scheme in allow:
            key = random_key()
            cache.add(key, url)
            context = {'message': 'Your link is  ', 'link': 'http://127.0.0.1:8000/' + key}
            return render(request, 'index.html', context)
        else:
            context['message'] = 'Only https, http, ftp addresses excepted!'
            return render(request, 'index.html', context)


def redirect_view(request, key):
    """
    Функция обрабатывает сокращенный URL вида http://localhost:8000/<key>
    Ищем ключ в кеше (cache.get). Если ключ не найден,
    редиректим на главную страницу (/). Если найден,
    редиректим на полный URL, сохраненный под данным ключом.
    """
    redirect_url = cache.get(key)
    if redirect_url is None:
        return redirect(to='/')
    else:
        redirect(redirect_url)






def stats(request, key):
    """
    Статистика кликов на сокращенные ссылки.
    В теле ответа функция возращает количество
    переходов по данному коду.
    """
    pass


urlpatterns = [
    path('', index),
    path(r'stats/<key>', stats),
    path(r'<key>', redirect_view),
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
