from django.apps import AppConfig

class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # Sobreescrevendo a função READY de CARSCONFIG
    def ready(self):
        import cars.signals
