import csv

# Read the LastPass CSV file
with open('lastpass_export.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Define the Team Password Manager headers
team_password_headers = [
    'Name', 'Access information', 'Username', 'E-mail', 'Password', 'Notes',
    'Tags', 'Custom fields', 'Custom 1', 'Custom 2', 'Custom 3', 'Custom 4',
    'Custom 5', 'Custom 6', 'Custom 7', 'Custom 8', 'Custom 9', 'Custom 10'
]

# Create a new list of dictionaries to hold the transformed data
transformed_rows = []
for row in rows:
    transformed_row = {
        'Name': row['name'],
        'Access information': row['url'],
        'Username': row['username'],
        'E-mail': row['username'],  # Assuming E-mail is the same as Username
        'Password': row['password'],
        'Notes': row['extra'],
        'Tags': row['grouping'],
        'Custom fields': '',
        'Custom 1': '',
        'Custom 2': '',
        'Custom 3': '',
        'Custom 4': '',
        'Custom 5': '',
        'Custom 6': '',
        'Custom 7': '',
        'Custom 8': '',
        'Custom 9': '',
        'Custom 10': ''
    }
    transformed_rows.append(transformed_row)

# Write the transformed data to a new CSV file
with open('team_password_manager_import.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=team_password_headers)
    writer.writeheader()
    writer.writerows(transformed_rows)

print("Conversion complete. The file 'team_password_manager_import.csv' is ready for import.")