from celery import shared_task
from stats.models import IntagramStats

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@shared_task
def update_user_intagram_statistics():

    instagram_users = IntagramStats.objects.all()
    for instagram_user in instagram_users:

        # Set up the Selenium WebDriver
        driver = webdriver.Chrome() # Replace with appropriate WebDriver for your browser

        username = instagram_user.username
        password = instagram_user.password

        # Navigate to Instagram login page
        driver.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))  # Wait for page to load

        # Enter login credentials
        username_input = driver.find_element(By.NAME, 'username')
        username_input.send_keys(username)  # Replace with your Instagram username
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)  # Replace with your Instagram password
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        sleep(10)

        not_now_button = driver.find_element(By.XPATH, "//div[contains(text(),'Not Now')]")
        not_now_button.click()

        sleep(3)

        not_now_button = driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
        not_now_button.click()

        # Navigate to user's profile page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/{username}/']")))  # Wait for profile page to load
        profile_button = driver.find_element(By.XPATH, f"//a[@href='/{username}/']")
        profile_button.click()

        # Retrieve follower count
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/{username}/followers/']")))  # Wait for follower count to load
        follower_count_element = driver.find_element(By.XPATH, f"//a[@href='/{username}/followers/']")
        follower_count = follower_count_element.text

        # Retrieve following count
        following_count_element = driver.find_element(By.XPATH, f"//a[@href='/{username}/following/']")
        following_count = following_count_element.text

        instagram_stats, created = IntagramStats.objects.get_or_create(username=username)
        instagram_stats.follower = int(follower_count.split(' ')[0])
        instagram_stats.following = int(following_count.split(' ')[0])
        instagram_stats.save()

        # # Close the browser window
        driver.quit()


    
