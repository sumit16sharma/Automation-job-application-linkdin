from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Sumit\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

LOGIN_URL ="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
EMAIL = "devilfromhell16@gmail.com"
PASSWORD = "mautkakhel"

driver.get(url=LOGIN_URL)

driver.implicitly_wait(5)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

email = driver.find_element_by_name("session_key")
email.send_keys(EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.implicitly_wait(5)

not_now = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button')
not_now.click()



