import speech_recognition as sr
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

r = sr.Recognizer()
data = sr.AudioFile('speech.wav')
with data as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language="en-IN")
    print(text)

if "open" in text:
    if "Chrome" in text:
        os.system("python open.py chrome")
        
    if "Brave" in text or "brave" in text:
        os.system("python open.py brave")
    if "settings" in text or "system settings" in text:
        os.system(" python open.py settings")
    if "file manager" in text or "file browser" in text or "File Manager" in text or "File Browser" in text or "files" in text or "Files" in text:
        os.system(" python open.py filemanager")

        
if "play" in text:
        print("play in text")
        text = text.replace("play", "")
        if text=="" or text==" ":
            print("No name specified!!")
        else:
            text = text.replace("on YouTube", "")
            print("Recived : "+text)
            driver = webdriver.Firefox(executable_path="/home/garuda/Github projects/Virtual-assistant/geckodriver")
            driver.implicitly_wait(5)

            # Let's create a list of terms to search for and an empty list for links
            search_terms = [text]
            links = []

            for term in search_terms:
                # Open YouTube page for each search term
                driver.get('https://www.youtube.com/results?search_query={}'.format(term))
                # Find a first webelement with video thumbnail on the page
                link_webelement = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
                # Grab webelement's href, this is your link, and store in a list of links:
                links += [link_webelement.get_attribute('href')]
            
if "shutdown" in text or "shut down" in text:
    input("Really ?")
    os.system("shutdown")

else:
    print("no useful commands found")    


print(links)
driver.quit()
os.system("google-chrome-stable "+links[0])

print("2 done")
