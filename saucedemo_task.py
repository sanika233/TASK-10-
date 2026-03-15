# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_and_fetch_details():

    # Launch browser
    driver = webdriver.Chrome()

    # Open website
    driver.get("https://www.saucedemo.com/")

    # Fetch title
    title = driver.title
    print("Page Title:", title)

    # Login credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    # Fetch current URL
    current_url = driver.current_url
    print("Current URL:", current_url)

    # Extract entire page source
    page_content = driver.page_source

    # Save content into text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_content)

    print("Page content saved successfully")

    driver.quit()

# Run function
login_and_fetch_details()