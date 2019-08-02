"""
    the import below does not import the AUTH_USER_MODEL from settings, which normally is done for reuseable apps
    the reason for this is that this backend will only work with the PS2User
"""
from ps2auth.models import PS2User

import logging


class PS2AuthBackend(object):

    def authenticate(self, email, password):
        try:
            user = PS2User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except PS2User.DoesNotExist:
            logging.getLogger("error_logger").error("User with login {} does not exist.".format(email))
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = PS2User.objects.get(id=user_id)
            if user.is_active:
                return user
        except PS2User.DoesNotExist:
            logging.getLogger("error_logger").error("User with USER_ID {} does not exist.".format(user_id))
            return None