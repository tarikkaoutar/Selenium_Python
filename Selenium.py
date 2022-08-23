from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
URL = 'https://www.adamchoi.co.uk/overs/detailed'
# Path = 'C:/Users/mrtar/Downloads/chromedriver_win32/chromedriver/chromedriver.exe'
driver = webdriver.Chrome('C:/Users/mrtar/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(URL)
# 
driver.maximize_window()
# click button
All_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
All_matches_button.click()
# storage data in lists
times = []
teams_1 = []
teams_2 = []
results = []
# dropdown Selecting
dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
# implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
time.sleep(3)
# select elements in the table
tables = driver.find_elements(By.TAG_NAME,'tr')


# select element in table
for table in tables:
    time = table.find_element(By.XPATH,'./td[1]').text
    times.append(time)
    team_1 = table.find_element(By.XPATH,'./td[2]').text
    teams_1.append(team_1)
    team_2 = table.find_element(By.XPATH,'./td[3]').text
    teams_2.append(team_2)
    result = table.find_element(By.XPATH,'./td[4]').text
    results.append(result)
driver.quit()

# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'date': times, 'home_team': teams_1, 'score': results, 'away_team': teams_2})
df.to_csv('football_data_Spain.csv', index=False)
# print(df)

