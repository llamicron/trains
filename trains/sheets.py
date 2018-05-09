from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogleSheets(object):
    """
    Custom interface for getting simple data out of Google Sheets
    """
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



google = GoogleSheets()

# Training Codes
trainings = []
keys = ['id', 'code', 'title']
for record in google.get_sheet_data('training_codes!A2:C'):
    trainings.append(dict(zip(keys, record)))

# Role Codes
roles = []
keys = ['id', 'code', 'title']
for record in google.get_sheet_data('role_codes!A2:C'):
    roles.append(dict(zip(keys, record)))

# Volunteers
volunteers = []
rows = google.get_sheet_data('volunteers!A:S')
keys = [s.lower() for s in rows[0]]
for values in rows[1:]:
    volunteers.append(dict(zip(keys, values)))

# How to use:
# from sheets import volunteers, trainings, roles
