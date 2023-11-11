from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
 
lat = [37.3618461,37.3490862,37.3545187]
lon = [140.3679248, 140.3627885,140.3647392]
CHROMEDRIVER = 'C:/Users/andoy/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'    

    
options = Options()
options.add_argument('--hide-scrollbars')
options.add_argument('--incognito')
options.add_argument('--headless')
 
service = Service(executable_path=CHROMEDRIVER)
#driver = webdriver.Chrome(CHROMEDRIVER, options=options)
driver = webdriver.Chrome(options=options, service=service)
driver.set_window_size(1920, 1080)

for i in range(len(lat)):
    URL = "https://www.google.com/maps/@"+str(lat[i])+","+str(lon[i])+",101m/data=!3m1!1e3?entry=ttu"
    driver.get(URL)
    time.sleep(1)
    elem = driver.find_element(By.XPATH, '//*[@id="minimap"]/div/div[2]/button')
    elem.click()
    elem = driver.find_element(By.XPATH, '//*[@id="layer-switcher-quick"]/div/div/div/ul/li[5]/button')
    elem.click()
    elem = driver.find_element(By.XPATH, '//*[@id="layer-switcher"]/div/div/div/div[3]/ul/li[2]/div/button/div')
    elem.click()
    elem = driver.find_element(By.XPATH, '//*[@id="layer-switcher"]/div/div/div/div[4]/ul/li[2]/button/div[1]')
    elem.click()
    time.sleep(1)
    driver.save_screenshot('result'+str(i)+'.png')
driver.quit()
    
