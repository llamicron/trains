from sheets import GoogleSheets

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


def main():
    return "Here's the entry point"
