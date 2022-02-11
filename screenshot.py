from lib2to3.pgen2 import driver
from selenium import webdriver 
from time import sleep 

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

browser = webdriver.Chrome('chromedriver.exe', chrome_options=options) 
browser.get("http://intranet.saude.ba.gov.br/") 
browser.execute_script("document.body.style.zoom='90%'")
browser.set_window_size(1920,1080,browser.window_handles[0])
browser.maximize_window()
print(browser.title)
sleep(5) 
browser.get_screenshot_as_file(browser.title + "_screenshot.png") 
browser.quit() 