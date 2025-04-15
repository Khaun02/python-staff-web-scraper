# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Define the list of school directories with names and URLs
schools = [
    {"name": "La Follette High School", "url": "https://lafollette.madison.k12.wi.us/contact-us"},
    {"name": "East High School", "url": "https://east.madison.k12.wi.us/contact-us"},
    {"name": "West High School", "url": "https://west.madison.k12.wi.us/contact-us"},
    {"name": "Memorial High School", "url": "https://memorial.madison.k12.wi.us/contact-us"},
    {"name": "Capital High School", "url": "https://capital.madison.k12.wi.us/contact-us"},
    {"name": "Shabazz High School", "url": "https://shabazz.madison.k12.wi.us/contact-us"}
]

# Define keywords that indicate relevant staff roles
target_keywords = [
    'counselor', 'principal', 'admin', 'secretary', 'assistant', 'ed asst', 'academic & career',
    'career plan', 'learning coord', 'instructional coach', 'mtss', 'student engagement',
    'psychologist', 'social worker', 'avid', 'uw people program', 'rest just', 'brs-', 'multicultural'
]

# Set up ChromeDriver path
service = Service(executable_path="/Users/shaunkhang/Downloads/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

# List to collect all staff entries
all_contacts = []

# Loop through each school and scrape their staff page
for school in schools:
    driver.get(school['url'])
    time.sleep(2)

    while True:
        time.sleep(2)
        staff_cards = driver.find_elements(By.CLASS_NAME, "fsConstituentItem")

        for card in staff_cards:
            try:
                name = card.find_element(By.CLASS_NAME, "fsFullName").text.strip()
                role = card.find_element(By.CLASS_NAME, "fsTitles").text.strip()
                email = card.find_element(By.CSS_SELECTOR, "a[href^='mailto:']").text.strip()

                # Only include staff whose role matches your target keywords
                if any(keyword in role.lower() for keyword in target_keywords):
                    all_contacts.append({
                        "name": name,
                        "role": role,
                        "email": email,
                        "school": school['name']
                    })
            except:
                continue

        # Try to go to the next page if it exists
        try:
            next_button = driver.find_element(By.CLASS_NAME, "fsNextPageLink")
            next_button.click()
        except:
            break  # Exit the while loop if no next button

# Close the browser when done
driver.quit()

# Convert results to a DataFrame and save to CSV
df = pd.DataFrame(all_contacts)
df.to_csv("s-stem_school_contacts.csv", index=False)
print("✅ Contacts saved to s-stem_school_contacts.csv")
