from django.apps import AppConfig


class BagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals