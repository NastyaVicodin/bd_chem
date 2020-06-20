from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('storage', 'v1', credentials=credentials)

filename = '~/abacipharma.csv'
bucket = 'chem_project_bucket'

body = {'name': 'abacipharma_data.csv'}
req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
resp = req.execute()
