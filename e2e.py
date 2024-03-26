import subprocess
import sys
import time

flask_process = subprocess.Popen(['C:\\Users\\OfriZacks\\PycharmProjects\\wog\\Scripts\\python.exe', 'main_score.py'])
time.sleep(3)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
def test_scores_service():
    service1 = Service()
    driver = webdriver.Chrome(service=service1)

    driver.maximize_window()
    driver.get("http://localhost:30000/")
    time.sleep(5)

    # validating no error page
    try:
        driver.find_element(By.ID, "score")
        print("element has been found")
    except NoSuchElementException:
        print("score page is INVALID")

    # validating the score is between 1 to 1000
    web_score = driver.find_element(By.ID, "score").text
    web_score = int(web_score)
    valid_score = True
    try:
        assert 1 <= web_score <= 1000, "the score is not between 1 to 1000"
    except AssertionError as error:
        print(error)
        valid_score = False
    return valid_score

def main_function():
    main_valid_score = test_scores_service()
    if main_valid_score:
        sys.exit(0)
    else:
        sys.exit(-1)

main_function()