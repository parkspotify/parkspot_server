"""
    the import below does not import the AUTH_USER_MODEL from settings, which normally is done for reuseable apps
    the reason for this is that this backend will only work with the PS2User
"""
from ps2auth.models import PS2User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password

from .models import Token

import logging, sys


class PS2AuthBackend(object):

    @staticmethod
    def authenticate(request, email, password=None, token=None):
        if token is not None:
            return PS2User.objects.get(auth_token=token)
        try:
            password = make_password(password)
            if PS2User.objects.exists(email=email):
                user = PS2User.objects.get(email=email)
                if check_password(password=password, encoded=user.password):
                    return user
                else:
                    return None
            else:
                user = PS2User.objects.create_user(email=email, password=password)
            if user:
                return user
        except PS2User.DoesNotExist:
            logging.getLogger(__name__).debug("User with login {} does not exist.".format(email))
            return "UserDoesNotExit"
        except Exception as e:
            logging.getLogger("stdout_logger").debug(repr(e))
            return repr(e)

    def get_user(self, email):
        try:
            user = PS2User.objects.get(email=email)
            if user.is_active:
                return user
        except PS2User.DoesNotExist:
            logging.getLogger("stdout_logger").debug("User with USER_ID {} does not exist.".format(email))
            return None

    def test_authenticate(self, email, password):
        try:
            user, created = PS2User.objects.get_or_create(email=email)
            if created:
                user.set_password(raw_password=password)
                return user
            elif not created and check_password(password=password, encoded=user.password):
                return user.check_password(password)
            else:
                return None
        except PS2User.DoesNotExist:
            logging.getLogger(__name__).debug("User with login {} does not exist.".format(email))
            return "UserDoesNotExit"
        except Exception as e:
            logging.getLogger("stdout_logger").debug(repr(e))
            return repr(e)
