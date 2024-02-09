from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.99acres.com/property-rates-and-price-trends-in-kolkata-prffid?preference=RENTAL")



#########################
time.sleep(100)

elements = driver.find_elements(By.CLASS_NAME, 'rT__ptTuple')

# Extract data from elements
data_list = [element.text.strip() for element in elements]

# Print or process the extracted data with a separator
separator = '-' * 50  # You can adjust the number of dashes as needed


with open("data.txt",'a', encoding='utf-8') as file:
    for data in data_list:
        file.write(data)
        file.write(separator)
        file.write("\n")
    
    


# Close the browser window
driver.quit()