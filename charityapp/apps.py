from django.apps import AppConfig


class CharityappConfig(AppConfig):
    name = 'charityapp'

    def ready(self):
        import charityapp.signals