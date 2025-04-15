from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Step 1: Set up ChromeDriver
service = Service(executable_path="/Users/shaunkhang/Downloads/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

# Step 2: Open the La Follette staff directory page
driver.get("https://lafollette.madison.k12.wi.us/contact-us")
time.sleep(2)

# Step 3: Create a set to store unique titles
unique_titles = set()

# Step 4: Loop through all pages
while True:
    time.sleep(2)  # Wait for content

    # Step 5: Find all role elements by class name
    title_elements = driver.find_elements(By.CLASS_NAME, "fsTitles")

    # Step 6: Extract the text from each title element
    for element in title_elements:
        title_text = element.text.strip().lower()
        if title_text:
            unique_titles.add(title_text)

    # Step 7: Click the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.CLASS_NAME, "fsNextPageLink")
        next_button.click()
    except:
        break  # No more pages

# Step 8: Close the browser
driver.quit()

# Step 9: Print out all unique titles
print("\n📋 All unique staff roles found:")
for title in sorted(unique_titles):
    print(f"• {title}")
