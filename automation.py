import os
import shutil
import re
import requests
import logging

# ----------------------------
# Logging Setup
# ----------------------------
logging.basicConfig(
    filename="output/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create output folder
os.makedirs("output", exist_ok=True)


# ----------------------------
# Move JPG Files
# ----------------------------
def move_jpg_files():
    source = "images"
    destination = "moved_images"

    os.makedirs(destination, exist_ok=True)

    moved = 0

    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            shutil.move(
                os.path.join(source, file),
                os.path.join(destination, file)
            )
            moved += 1

    print(f"\n✅ {moved} JPG files moved successfully.")
    logging.info(f"{moved} JPG files moved.")


# ----------------------------
# Extract Emails
# ----------------------------
def extract_emails():

    with open("sample.txt", "r") as file:
        text = file.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    with open("output/emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"\n✅ {len(emails)} Emails extracted.")
    logging.info(f"{len(emails)} emails extracted.")


# ----------------------------
# Scrape Website Title
# ----------------------------
def scrape_title():

    url = "https://example.com"

    response = requests.get(url)

    title = re.search(
        r"<title>(.*?)</title>",
        response.text,
        re.IGNORECASE
    )

    if title:

        with open("output/title.txt", "w") as file:
            file.write(title.group(1))

        print("\n✅ Website title saved.")
        logging.info("Website title saved.")

    else:
        print("\n❌ Title not found.")
        logging.warning("Title not found.")


# ----------------------------
# Main Menu
# ----------------------------
while True:

    print("\n=========== TASK AUTOMATION ===========")

    print("1. Move JPG Files")
    print("2. Extract Emails")
    print("3. Scrape Website Title")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        move_jpg_files()

    elif choice == "2":
        extract_emails()

    elif choice == "3":
        scrape_title()

    elif choice == "4":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")