from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import datetime
from datetime import datetime as datetime_
import datetime

print("Start time: ")
print(datetime_.now())

############################################################################

# Chrome Driver Init
options = webdriver.ChromeOptions() 
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Waiter with a 30 seconds timeout
wait = WebDriverWait(driver, 30)

############################################################################

try:
    # Time Measurement Login
    start_time_login = datetime.datetime.now()

    # Get Front Page
    driver.get("")

    # # Wait until Login Form
    wait.until(EC.presence_of_element_located((By.ID, "i0116")))
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))

    # # Login
    username = driver.find_element_by_id("i0116")

    username.send_keys("")
    driver.find_element_by_id("idSIButton9").click()

    wait.until(EC.presence_of_element_located((By.ID, "passwordInput")))
    wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    password = driver.find_element_by_id("passwordInput")
    password.send_keys("")
    driver.find_element_by_id("submitButton").click()
    
    # # Wait until Page Load
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Approval Hub ->"]')))

    end_time_login = datetime.datetime.now()
    login_duration_ms = (end_time_login - start_time_login).total_seconds() * 1000.0
    login_success = True

except NoSuchElementException as e:
    error_message_login = repr(e)

except TimeoutException as e:
    error_message_login = repr(e)

except Exception as e:
    error_message_login = repr(e)

############################################################################

print("End time: ")
print(datetime_.now())

driver.close()
driver.quit()

############################################################################