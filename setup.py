import os
import time

def main():
    if os.path.exists("installationRegistrary") == False:

        print("This script may require sudo permissions...")
        print("Downloading.....")
        time.sleep(1)
        print("Please be patient...")
        time.sleep(1)
        print("This may take a while...")

        if os.path.exists("model"):
            print("[*] models folder already exists...aborting installation")

        else:
            link="http://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
            os.system("wget http://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip")

            print("[*] Donwloaded!")
            print("[*] unzipping...")

            os.system("unzip vosk-model-small-en-us-0.15.zip")

            os.system("mv vosk-model-small-en-us-0.15 model")

        time.sleep(1)
        print("[*] downloading required python modules...")
        os.system("pip install webrtcvad")
        os.system("pip install SpeechRecognition vosk pyaudio")

        concern = input("Do you want to install speech systhesis(This will require docker to be installed) ? [yes | y | no | n] ")

        if concern == "yes" or concern == "y":
            print("installing speech systhesis...")
            time.sleep(1)
            print("pls give sudo permission")
            time.sleep(2)
            print("using docker...")
            print("[*] Requesting sudo permission")
            os.system("sudo docker run -it -p 5002:5002 rhasspy/larynx:en-us")
            f= open("installationRegistrary","w+")
        else:
            print("Selected option no. Finishing script")
            f= open("installationRegistrary","w+")
            f.close()

    else:
        if os.path.exists("installationRegistrary") == True:
            print("Hey user, a registrary has been registered. If you think there is a mistake, you can delete the installationRegistrary file")

            
main()
