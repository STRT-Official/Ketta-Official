from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium
import re
import time
import os
from playsound import playsound

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def searchWEB(query):
	try:
		driver.get("https://search.brave.com/search?q="+query+"&source=desktop")
		time.sleep(2)
		child_elem1 = driver.find_element("xpath", "/html/body/main/div[2]/div[1]/div[1]/div/div[2]/span[1]")
		child_elem2 = driver.find_element("xpath", "/html/body/main/div[2]/div[1]/div[1]/div/div[2]/span[2]")

		#print(child_elem1.get_attribute('innerHTML'))

		string1 = str(child_elem1.get_attribute('innerHTML'))
		string2 = str(child_elem2.get_attribute('innerHTML'))

		result1 = re.sub(r'<(.+?)>', '', string1)
		result1 = result1[:-1]
		result2 = re.sub(r'<(.+?)>', '', string2)
		result2 = result2[:-1]
		result = ' '.join([result1, result2])
		print(result)
		with open("tospeak.txt", "w") as speak_file:
			speak_file.write(result)
		os.system("bash voice_syn.sh")
		playsound("output.wav")
		
	except selenium.common.exceptions.NoSuchElementException:
		print("No results on Brave search")
		driver.get("https://www.bing.com/search?q="+query)
		time.sleep(2)
		input("waiting")
		elem = driver.find_element("xpath", "/html/body/div[2]/main/ol/li[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]")
		string = str(elem.get_attribute('innerHTML'))
		result = re.sub(r'<(.+?)>', '', string)
		##result = result[:-1]
		print(result)
		with open("tospeak.txt", "w") as speak_file:
			speak_file.write(result)
		os.system("bash voice_syn.sh")
		playsound("output.wav")
