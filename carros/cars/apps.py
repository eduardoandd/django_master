from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    
    # carrega signals ao inciar a aplicação, deixando disponível o signals para o app.
    def ready(self):
        import cars.signals
