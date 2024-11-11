from django.shortcuts import render


def page_not_found(request, exception):
    """Подключение кастомной страницы Ошибка 404: страница не найдена."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """403: ошибка проверки CSRF, запрос отклонён."""
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    """500: ошибка сервера."""
    return render(request, 'pages/500.html', status=500)
