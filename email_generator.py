import csv
import random
import string

# Function to generate a random email address
def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com"]
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Generate 100 random email addresses
random_emails = [generate_random_email() for _ in range(100)]

# Define the CSV file name
csv_file = "random_emails.csv"

# Write the random email addresses to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    for email in random_emails:
        writer.writerow([email])

print(f"Random emails saved to {csv_file}")
