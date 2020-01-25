from django.apps import AppConfig


class EducationConfig(AppConfig):
    name = 'Education'
    def ready(self):
        import Education.mysignal

