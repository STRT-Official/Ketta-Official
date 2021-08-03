import os
import sys
import subprocess

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if "chrome" in str(sys.argv):
    print("chrome is there")
    subprocess.Popen("google-chrome-stable")

if "Brave" in str(sys.argv) or "brave" in str(sys.argv):
    print("brave is there")
    subprocess.Popen("brave")
    
if "settings" in str(sys.argv):
    print("opening settings")
    subprocess.Popen("systemsettings5")

if "filemanager" in str(sys.argv):
    print("opening file manager")
    subprocess.Popen("dolphin")
    
