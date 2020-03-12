from __future__ import print_function

from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('./storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('./client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

#files = DRIVE.files().list().execute().get('files', [])
#for f in files:
 #   print(f['name'], f['mimeType'])

upload_folder =DRIVE.files().list(orderBy='createdTime desc',q="mimeType='application/vnd.google-apps.folder'").execute().get('files',[])
f=upload_folder[0]['id']

def uploadFile(filename):
    file_metadata = {
    'name': filename,
    'mimeType': '*/*',
    'parents':[f]
    }
    media = MediaFileUpload(filename,
                            mimetype='*/*',
                            resumable=True)
    file = DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
    #print ('File ID: ' + file.get('id'))
