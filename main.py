from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up your ChromeDriver path
service = Service(executable_path="/Users/shaunkhang/Downloads/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

# Open the La Follette staff directory
driver.get("https://lafollette.madison.k12.wi.us/contact-us")
time.sleep(2)

# Keywords for filtering relevant staff roles
target_keywords = [
    "counselor",
    "principal",
    "admin",
    "secretary",
    "assistant",
    "ed asst",
    "coach",  # Only if you're including AVID/restorative justice coaches
    "academic & career",
    "career plan",
    "learning coord",
    "instructional coach",
    "mtss",
    "student engagement",
    "psychologist",
    "social worker",
    "avid",
    "uw people program",
    "rest just",
    "brs-",
    "multicultural"
]

# List to hold results
email_list = []

# Loop through all pages by clicking the Next button
while True:
    time.sleep(2)  # Let page load

    staff_cards = driver.find_elements(By.CLASS_NAME, "fsConstituentItem")

    for card in staff_cards:
        try:
            name = card.find_element(By.CLASS_NAME, "fsFullName").text.strip()
            role = card.find_element(By.CLASS_NAME, "fsTitles").text.strip()
            email = card.find_element(By.CSS_SELECTOR, "a[href^='mailto:']").text.strip()

            if any(keyword in role.lower() for keyword in target_keywords):
                email_list.append({
                    "name": name,
                    "role": role,
                    "email": email,
                    "school": "La Follette High School"  # ✅ Added school name
                })
        except Exception as e:
            print(f"Skipping a card: {e}")
            continue

    # Try to find the "Next" button
    try:
        next_button = driver.find_element(By.CLASS_NAME, "fsNextPageLink")
        next_button.click()
    except:
        print("No more pages. Finished scraping.")
        break  # Exit loop when Next is no longer present

# Close the browser
driver.quit()

# Print results
for person in email_list:
    print(person)

# Optional: save to CSV
df = pd.DataFrame(email_list)
df.to_csv("lafollette_admin_contacts.csv", index=False)
