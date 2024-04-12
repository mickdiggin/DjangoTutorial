# INF601 - Advanced Programming in Python
# Michael DeGan
# Mini Project 4

from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
