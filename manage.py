#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject1Afternoon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



#slashi sorus urllerde


# gitden clone edib run problemi

# Template-ə ötürülən məlumat dəstidir.

# Yəni View → Template arasında daşınan dict tipli obyekt.


# render() → HTML cavabı üçün “ready-made” qısa yol.

# render() = sadəcə HTML üçündür.



# 1. Route Params (URL Parameters / Path Parameters)
#
# Bunlar URL yolunun bir hissəsidir.
#
# Django-da path() içində <param> yazmaqla təyin olunur.
#
# Məqsəd: URL-dən dəyişən dəyər götürmək.
#
# Misal – views.py
#
# from django.http import HttpResponse
#
# def user_profile(request, user_id):
#     return HttpResponse(f"User ID: {user_id}")
#
#
# urls.py
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path("user/<int:user_id>/", views.user_profile),
# ]
#
#
# http://127.0.0.1:8000/user/5/ → user_id = 5
#
# http://127.0.0.1:8000/user/42/ → user_id = 42
#
# 👉 Bunlara route params və ya path params deyilir.