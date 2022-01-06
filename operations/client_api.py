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

        response =  requests.get(
            settings.APILOS_API_CLIENT_HOST + 'conventions/',
            auth=(
                settings.APILOS_API_CLIENT_USERNAME,
                settings.APILOS_API_CLIENT_PASSWORD,
            ),
            allow_redirects=True,
            params={'bailleur_uuid': '8e55ca3a-f7be-4f9d-8f66-7e12bfb8e7c5'}
        )
        return response.json()


        # print(settings.APILOS_API_CLIENT_HOST + 'conventions/')
        # return self.client.get(settings.APILOS_API_CLIENT_HOST + 'conventions?bailleur_uuid=2c84b275-4a82-4524-958b-b405abb5f5f8')

    def create_programme(self, payload):
        print(f"CREATE PROGRAMME : {settings.APILOS_API_CLIENT_HOST + 'programmes/'}")
        programme = requests.post(
            settings.APILOS_API_CLIENT_HOST + 'programmes/',
            auth=(
                settings.APILOS_API_CLIENT_USERNAME,
                settings.APILOS_API_CLIENT_PASSWORD,
            ),
            allow_redirects=False,
            data=payload
        )
        print(programme)
        if programme.status_code == 201:
            return programme.json()

    def create_lot(self, payload):
        print(f"CREATE LOT : {settings.APILOS_API_CLIENT_HOST + 'lots/'}")
        lot = requests.post(
            settings.APILOS_API_CLIENT_HOST + 'lots/',
            auth=(
                settings.APILOS_API_CLIENT_USERNAME,
                settings.APILOS_API_CLIENT_PASSWORD,
            ),
            allow_redirects=False,
            data=payload
        )
        if lot.status_code == 201:
            return lot.json()






