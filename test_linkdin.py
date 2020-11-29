import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
import selenium

profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.download.dir", DOWNLOAD_DIR_TMP)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.openFile","application/msword")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/msword")
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("pdfjs.disabled", True)
profile.set_preference("browser.download.manager.focusWhenStarting", False)

browser=webdriver.Firefox(profile)
browser.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
time.sleep(2)

btn_iniciar_sesion = '/html/body/div/main/div[2]/form/div[3]/button'
wait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, btn_iniciar_sesion)))

browser.find_element_by_id('username').send_keys('Atencioncliente@zigma.cl')
time.sleep(2)
browser.find_element_by_id('password').send_keys('diagonal1374')
time.sleep(2)
browser.find_element_by_xpath(btn_iniciar_sesion).click()

#/html/body/div[7]/header/div[2]/div/div/div[1]/div[1]/input
#/html/body/div[8]/header/div[2]/div/div/div[1]/div/input

i=0
continuar = False
while i<60 and continuar==False:
	i = 1 + 1
	try:
		input_buscar = '/html/body/div[8]/header/div[2]/div/div/div[1]/div/input'
		wait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, input_buscar)))
		continuar = True
	except:
		continuar = False

	if continuar==False:
		try:
			input_buscar = '/html/body/div[7]/header/div[2]/div/div/div[1]/div/input'
			wait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, input_buscar)))
			continuar = True
		except:
			continuar = False

browser.find_element_by_xpath(input_buscar).send_keys('tuberias')
browser.find_element_by_xpath(input_buscar).send_keys(Keys.ENTER)
time.sleep(2)

wait(browser, 60).until(EC.element_to_be_clickable((By.ID, 'ember629'))).click()

time.sleep(20)
