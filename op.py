import glob
import os
import subprocess
import sys
from playsound import playsound


def opening(filepath, appname):
	# Search for desktop entry matching the given keyword
	entries = []
	for root, _, files in os.walk(filepath, topdown=False):
		for name in files:
			if appname in name:
				entries.append(os.path.join(root, name))

	if entries:
		print("Found entries:")
		for entry in entries:
			print(entry)
	else:
		print("No entries found")

	if entries:
		name_list = [str(entries[0]), str(entries[0]).lower()]
		name = str(entries[0]).replace(filepath, "")
		name = str(name).replace("/", "")
		with open("tospeak.txt", "w") as speak_file:
			speak_file.write(result)
		os.system("bash voice_syn.sh")
		playsound("output.wav")
		os.system("gtk-launch "+appname)
		exit(0)
	print("No entries found")

def speak_name(NAME):
	with open("tospeak.txt", "w") as speak_file:
		NAME = "opening " + NAME
		speak_file.write(NAME)
	os.system("bash voice_syn.sh")
	playsound("output.wav")
	
def openAPP(appName):
	print(appName)
	if "file manager" in appName:
		print("opening file manager")
		os.system("xdg-open / & disown")
		speak_name("file manager")
	if "browser" in appName:
		os.system("gtk-launch "+os.popen("xdg-settings get default-web-browser").read())
		speak_name("browser")
	if "gnome help" in appName:
		os.system("gtk-launch yelp")
		speak_name("gnome help")
	if "system settings" in appName:
		print("opening system settings")
		os.system("gnome-control-center & disown")
		speak_name("gnome control centre")
	if "maps" in appName:
		os.system("gtk-launch org.gnome.Maps")
		speak_name("maps")
	if "terminal" in appName:
		os.system("gtk-launch org.gnome.Terminal")
		speak_name("terminal")
	if "photos" in appName:
		os.system("gtk-launch org.gnome.Photos")
		speak("photos")
		

			
	else:
		appName = appName.replace(" ", "")
		opening("/home/strtsnm/.local/share/applications/", appName)
		opening("/usr/share/applications", appName)
		opening("/home/strtsnm/.local/share/applications/", appName[:1].upper() + appName[1:] if appName else "")
		opening("/usr/share/applications", appName[:1].upper() + appName[1:] if appName else "")


