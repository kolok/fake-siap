import requests
import coreapi
from django.conf import settings

class ClientAPI():
    def __init__(self):

        auth = coreapi.auth.BasicAuthentication(
            username=settings.APILOS_API_CLIENT_USERNAME,
            password=settings.APILOS_API_CLIENT_PASSWORD,
        )
        self.client = coreapi.Client(auth=auth)

    def get_conventions(self):
        print(settings.APILOS_API_CLIENT_HOST + 'conventions')
        return self.client.get(settings.APILOS_API_CLIENT_HOST + 'conventions')
