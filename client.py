import coreapi

auth = coreapi.auth.BasicAuthentication(
    username='sabine',
    password='M@r!n!13'
)
client = coreapi.Client(auth=auth)

programmes = client.get('http://local.beta.gouv.fr:8001/api/v1/programmes')

print(programmes)