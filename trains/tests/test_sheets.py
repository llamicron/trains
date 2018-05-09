import unittest

from .. import sheets
from ..sheets import GoogleSheets

class TestGoogleSheets(unittest.TestCase):
    def test_init(self):
        sheets = GoogleSheets()
        assert type(sheets) is GoogleSheets

        sheets = GoogleSheets(storage_file="test_credentials.json", secret_file="test_client_secret.json")
        assert type(sheets) is GoogleSheets

    def test_get_sheet_data(self):
        sheets = GoogleSheets()
        rows = sheets.get_sheet_data('unittest!A:C')
        assert len(rows) == 4
        assert len(rows[0]) == 3

        assert 'tests' in rows[1][2]

    def test_role_associations(self):
        roles = sheets.volunteer_roles
        assert '42' in roles['12101808']
        assert 'SK' in roles['12109793']
        assert set(['42', '75', '80', 'PT', 'SA']) == set(roles['2274896'])
