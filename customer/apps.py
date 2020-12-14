from django.apps import AppConfig
import time
import threading


def test_run():
    from django.contrib.auth.models import User
    from api.mail_user import send_subscriber_updates
    while(1):
        send_subscriber_updates()
        time.sleep(60)


class CustomerConfig(AppConfig):
    name = 'customer'

    def ready(self):
        import customer.signals

        thread = threading.Thread(target=test_run)
        thread.start()
