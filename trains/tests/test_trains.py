import unittest
from ..sheets import trainings, roles, volunteers

from .. import *


def test_entry_point():
    assert main() == "Here's the entry point"


def test_get_role_code():
    volunteer = {'council': 'Sam Houston Area Council 576', 'service_area': 'Frontier Division - SA06', 'district': 'Arrowmoon - 21', 'sub_district': '', 'unit': 'Pack 0976', 'chartered_org_name': 'Sul Ross PTO', 'first_name': 'Christopher', 'middle_name': 'Don', 'last_name': 'Abbott', 'zip_code': '77802', 'memberid': '133631808', 'program': 'Cub Scouts', 'registration_expiration_date': '12/31/2018',
                 'email': 'mail@er.ar', 'position': 'Den Leader', 'trained': 'NO', 'incomplete_mandatory': 'SCO_800', 'incomplete_classroom': 'C42', 'incomplete_online': 'SCO_230'}

    assert volunteer['position'] == 'Den Leader'
    assert role_code(volunteer) == 'DL'


def test_get_roles():
    pass
    assert volunteers
    li = get_roles(volunteers)
    # Training list looks like this:
    # {
    #     'memberid': ['A09', 'ABC', 'XYZ', '123']
    # }
    assert 'DL' in li['133631808']
    assert 'SA' in li['115467607']
    assert set(li['2274896']) == set(['42', '75', '80', 'PT', 'SA'])

    errors = []
    for memberid, roles in li.items():
        for role in roles:
            if not role:
                errors.append(memberid)
            assert role
