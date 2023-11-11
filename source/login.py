#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time



def login(username, password):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Navigate to the captive portal URL
        driver.get("http://192.168.2.1:8090/httpclient.html")

        # Find the username and password input fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Input your username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Sleep for a few seconds to allow the login to complete
        time.sleep(1)

    finally:
        # Close the browser
        driver.quit()

def auto_login(username, password, interval_minutes):
    while True:
        # Perform login
        login(username, password)

        # Sleep for the specified interval before attempting to login again
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Set your username and password
    username = "your-username"
    password = "your-password"

    # Set the interval for auto-login in minutes (e.g., 30 minutes)
    interval_minutes = 30

    # Start the auto-login loop
    auto_login(username, password, interval_minutes)
