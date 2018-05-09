from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogleSheets(object):
    def __init__(self, storage_file='credentials.json', secret_file='client_secret.json'):
        file_path = 'trains/data/'
        self.sheet_id = '1Qa_fuxmJKU84qfL1z73EcSpy-K2Z_JtecPSedWle9M8'

        SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        store = file.Storage(file_path + storage_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(file_path + secret_file, SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

    def get_sheet_data(self, RANGE):
        """
        RANGE includes the sheet name. Uses A1 form. Eg:
        volunteers!A:D
        is the 'volunteers' sheet, columns 'A' through 'D'.
        """
        assert type(RANGE) is str

        result = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=RANGE).execute()
        return result.get('values', [])
