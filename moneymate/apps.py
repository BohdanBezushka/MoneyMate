from django.apps import AppConfig


class MoneymateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moneymate'

    def ready(self):
        import moneymate.signals
