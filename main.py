from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datePrime import Message

PASSWORD = "wohxat-Jurmoz-0hiqxy"
USER_NAME = "is_today_prime1"

url = "https://twitter.com/i/flow/login/"
chrome_driver_path = "/Users/filiphome/development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(url)
time.sleep(2)
username = driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys(USER_NAME)
username.send_keys(Keys.ENTER)

time.sleep(4)

passw = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
passw.send_keys(PASSWORD)
time.sleep(1)
passw.send_keys(Keys.ENTER)
time.sleep(4)


message = Message()

text = f"{message.day} {message.is_prime(message.day)} a prime number. \n {message.month} " \
       f"{message.is_prime(message.month)} a prime number. \n{message.year} {message.is_prime(message.year)} " \
       f"a prime number. \n{message.d_m} {message.is_prime(message.d_m)} a prime number. \n{message.d_m_y} " \
       f"{message.is_prime(message.d_m_y)} a prime number. \n"


twitter_box = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")


twitter_box.send_keys(text)

time.sleep(3)

tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')

tweet_button.click()

time.sleep(40)
