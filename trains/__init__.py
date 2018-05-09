from .sheets import trainings, roles, volunteers

def role_code(volunteer):
    """
    Looks in google sheets for a record with a matching title, and return the associated code
    """
    for role in roles:
        if role['title'].lower() == volunteer['position'].lower():
            return role['code']

def get_roles(volunteers):
    """
    returns a `dict` like this:
    {
        'memberid': ['A09', 'ABC', 'XYZ', '123']
    }
    The data from my.scouting.org can only relate one volunteer to one role.
    There are duplicated volunteers, with a different postition in each record.
    This will associate each volunteer with the proper roles, and remove duplicates.

    Note: sometimes 'role' and 'position' are used interchangibly. I try to use role in the code.
    """
    role_list = {}
    for vol in volunteers:
        if not vol['memberid'] in role_list.keys():
            role_list[vol['memberid']] = []
        role_list[str(vol['memberid'])].append(role_code(vol))
    return role_list



def main():
    return "Here's the entry point"

