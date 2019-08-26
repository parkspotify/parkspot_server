import sys

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'p2auth.stdout_logger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}