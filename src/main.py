import subprocess
import os
import time


username = os.environ["HOME"].split("/")[-1] # usually the last item is the username so grab it. This assumes linux, since flatpak runs on linux only.

print(username) # debug

def installApp(flatpakApp):
    try:
        subprocess.run(["flatpak", "install", flatpakApp, "--assumeyes"])
    except Exception as e:
        print(f"Error installing {flatpakApp}. Details:\n", e)

try:
    os.mkdir(f"/home/{username}/.flatpaktransfer") # attempt to make a directory for the files to be transferred to
except:
    print("Directory already exists.")

current_files = os.listdir(f"/home/{username}/.flatpaktransfer") # initial setting of current files

def waitForFiles():
    while True:
        prev_files = current_files
        current_files = os.listdir(f"/home/{username}/.flatpaktransfer")
        for file in current_files:
            if file not in prev_files:
                if file.split(".")[-1] == "flatpakref": # detect if it is a flatpakref file
                    installApp(f"/home/{username}/.flatpaktransfer/{file}") # Absolute directory to allow running program in any pwd
        time.sleep(1) # sleep for a second to prevent excessive assignment of variables

print("Initializing...")


# TODO: async
def waitForPhone():
    try:
        subprocess.run(['adb', 'pull', '/sdcard/flatpaktransfer', f'/home/{username}/.flatpaktransfer'])
    except Exception as e:
        print(e) # it might be very bad so print just in case
    time.sleep(60) # sleep for a minute to wait for the phone to be connected
