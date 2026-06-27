import re

# Read text file
with open("sample.txt", "r") as file:
    text = file.read()

# Find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")