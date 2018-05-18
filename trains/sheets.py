from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class GoogleSheets(object):
    """
    Custom interface for getting simple data out of Google Sheets
    """

    def __init__(self, storage_file='credentials.json', secret_file='client_secret.json'):
        file_path = 'trains/'
        self.sheet_id = '1Qa_fuxmJKU84qfL1z73EcSpy-K2Z_JtecPSedWle9M8'

        SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        store = file.Storage(file_path + storage_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(
                file_path + secret_file, SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

    def get_sheet_data(self, RANGE):
        """
        RANGE includes the sheet name. Uses A1 form. Eg:
        volunteers!A:D
        is the 'volunteers' sheet, columns 'A' through 'D'.
        """
        assert type(RANGE) is str

        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.sheet_id, range=RANGE).execute()
        return result.get('values', [])


# Data proccessing
# Just getting it ready for actual use

google = GoogleSheets()

# Flat is better than nested.
# Namespaces are one honking great idea -- let's do more of those!
# - The Zen of Python, Tim Peters

# Get Volunteers
volunteers = []
rows = google.get_sheet_data('volunteers!A:S')
keys = [s.lower() for s in rows[0]]
for values in rows[1:]:
    volunteers.append(dict(zip(keys, values)))

# Get Training Codes
trainings = []
keys = ['id', 'code', 'title']
for record in google.get_sheet_data('training_codes!A2:C'):
    trainings.append(dict(zip(keys, record)))

# Get Role Codes
roles = []
keys = ['id', 'code', 'title']
for record in google.get_sheet_data('role_codes!A2:C'):
    roles.append(dict(zip(keys, record)))


def find_role_code(role_title):
    for role in roles:
        if role['title'] == role_title:
            return role['code']

# Merge duplicate volunteers
# from pprint import pprint
# memberids = set(list([i['memberid'] for i in volunteers]))
# for memberid in memberids:
#     duplicates = [vol for vol in volunteers if vol['memberid'] == memberid]
#     role_titles = [vol['position'] for vol in duplicates]
#     role_codes = [find_role_code(x) for x in role_titles]
#     print(role_codes)

#     vol = duplicates[0]
#     vol['roles'] = dict(zip(role_codes, role_titles))
#     if len(role_titles) > 1:
#         print(vol['roles'])



# people = []
# for vol in volunteers:
#     person = {
#         'memberid': vol['memberid'],
#         'name': vol['first_name'] + ' ' + vol['last_name'],
#         'email': vol['email'],
#         'roles': getRolesFor(vol['memberid']),
#         'trainings': getTrainingsFor(vol)
#     }




















# Associate roles with members, eg:
# {
#   'memberid': ['ABC', 'XYZ', '123']
# }
# This is basically a pivot table
# role_map = {}
# for vol in volunteers:
#     if not vol['memberid'] in role_map.keys():
#         role_map[vol['memberid']] = []

#     for role in roles:
#         if role['title'].lower() == vol['position'].lower():
#             role_map[str(vol['memberid'])].append(role['code'])
# assert role_map


# keys = ["incomplete_mandatory", "incomplete_classroom", "incomplete_online"]
# volunteer_trainings = {}
# for vol in volunteers:
#     for key in keys:
#         try:
#             vol[key] = [s.strip().upper() for s in vol[key].split(',')]
#         except KeyError:
#             vol[key] = []




# volunteers = [
#     {
#         'memberid': '123abcxyz',
#         'name': 'Luke Sweeney',
#         'email': 'test@test.test'
#         'role': {
#             'SK': "Skipper"
#         }
#         'trainings': {
#             'SCO_800': 'Youth Protection Training'
#         },
#     }
# ]

# roles = [
#     {
#         'code': 'SK',
#         'title': 'Skipper'
#     }
# ]
