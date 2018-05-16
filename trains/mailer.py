from sheets import volunteers, role_map, trainings
from pprint import pprint

# {
#     'memberid': '123abcxyz',
#     'email': 'test@test.test',
#     'trainings': ['Wood Badge'],
# }

class Mailer(object):
    def send(self, email_text, target_roles):
        assert email_text
        assert type(target_roles) is list
        # pprint(role_map)
        # pprint(volunteers[2])

        targets = []
        for memberid, roles in role_map.items():
            for role in roles:
                if role in target_roles:
                    vol = self.get_volunteer(memberid)
                    targets.append({
                        'memberid': memberid,
                        'name': vol['first_name'] + " " + vol['last_name'],
                        'email': vol['email'],
                        'role': vol['position'],
                        'trainings': self.get_training_titles(vol)
                    })


        # Filter targets without emails or trainings
        targets = [t if t['trainings'] and t['email'] else None for t in targets]
        targets = list(filter(None.__ne__, targets))





    def get_volunteer(self, memberid):
        for vol in volunteers:
            if str(vol['memberid']).upper() == str(memberid).upper():
                return vol

    def get_training_titles(self, volunteer):
        titles = []
        for training in trainings:
            if training['code'] in volunteer['incomplete_mandatory']:
                titles.append(training['title'])
        return titles
