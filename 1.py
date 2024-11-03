import csv

# Define the list to store users from Barcelona
users_in_barcelona = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        # Check if the user is from Barcelona
        if 'barcelona' in location:
            users_in_barcelona.append({
                'login': row['login'],
                'followers': int(row['followers'])
            })

# Sort users based on followers in descending order
top_users = sorted(users_in_barcelona, key=lambda x: x['followers'], reverse=True)

# Extract the top 5 user logins
top_5_logins = [user['login'] for user in top_users[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_logins))
