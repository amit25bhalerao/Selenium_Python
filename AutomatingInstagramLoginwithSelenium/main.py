from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def create_driver(chrome_driver_path):
    # Start the ChromeDriver service
    service = webdriver.chrome.service.Service(chrome_driver_path)
    service.start()

    # Create a new Chrome browser instance
    driver = webdriver.Chrome(service=service)
    return driver


def login(driver, username, password):
    # Navigate to Instagram's login page
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login page to load
    time.sleep(5)

    # Find the username and password input fields by name
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    # Input your username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Press Enter to submit the login form
    password_input.send_keys(Keys.ENTER)

    # Wait for the login process to complete (you can add more time if needed)
    time.sleep(5)


def open_tag_page(driver, tag):
    driver.get("https://www.instagram.com/explore/tags/" + tag)
    time.sleep(5)


def scroll_down(driver, num_scrolls):
    try:
        for _ in range(num_scrolls):
            # Scroll down to load more posts
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
    except Exception as e:
        print("Error: ", e)


def select_home(driver):
    # Navigate to the home page
    driver.get("https://www.instagram.com/")
    time.sleep(5)


def open_reels(driver):
    # Navigate to the reels page
    driver.get("https://www.instagram.com/reels/")
    time.sleep(5)


def check_messages(driver):
    # Navigate to the messages inbox
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(5)


def check_notifications(driver):
    # Navigate to the notifications page
    driver.get("https://www.instagram.com/accounts/activity/")
    time.sleep(5)


# Example usage:
if __name__ == "__main__":
    username = "PleaseEnterUsername"
    password = "PleaseEnterPassword"
    tag_to_explore = "PleaseEnterHashtag"

    chrome_driver_path = "C:\chromedriver\chromedriver.exe"
    driver = create_driver(chrome_driver_path)
    try:
        login(driver, username, password)
        open_tag_page(driver, tag_to_explore)
        scroll_down(driver, num_scrolls=2)
        select_home(driver)
        open_reels(driver)
        check_messages(driver)
        check_notifications(driver)
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        driver.quit()
