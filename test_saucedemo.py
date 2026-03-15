from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_valid_login():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    # Verify Title
    assert "Swag Labs" in driver.title

    # Login
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    time.sleep(3)

    # Verify dashboard URL
    assert "inventory" in driver.current_url

def test_invalid_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    # Invalid login
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    error = driver.find_element(By.XPATH, "//h3").text

    assert "Epic sadface" in error

    driver.quit()
