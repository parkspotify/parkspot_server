# All settings concerning the Django Rest Framework: (these are imported into settings.py in parkspot2)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}