import subprocess
import os
import time


username = os.environ["HOME"].split("/")[-1] # usually the last item is the username so grab it. This assumes linux, since flatpak runs on linux only.

print(username) # debug

def installApp(flatpakApp):
    try:
        installProcess = subprocess.Popen(["flatpak", "install", flatpakApp, "--assumeyes"])
        installProcess.wait()
    except Exception as e:
        print(f"Error installing {flatpakApp}. Details:\n", e)

try:
    os.mkdir(f"/home/{username}/.flatpaktransfer") # attempt to make a directory for the files to be transferred to
    os.mkdir(f"/home/{username}/.flatpaktransfer/flatpaktransfer")
except:
    print("Directory already exists.")

current_files = os.listdir(f"/home/{username}/.flatpaktransfer/flatpaktransfer") # initial setting of current files

def checkForFiles():
    global current_files
    current_files = os.listdir(f"/home/{username}/.flatpaktransfer/flatpaktransfer")
    for file in current_files:
        if file.split(".")[-1] == "flatpakref": # detect if it is a flatpakref file
            installApp(f"/home/{username}/.flatpaktransfer/flatpaktransfer/{file}") # Absolute directory to allow running program in any pwd
            os.remove(f"/home/{username}/.flatpaktransfer/flatpaktransfer/{file}") # delete the file when we are done

print("Initializing...")

def waitForPhone():
    while True:
        try:
            result = subprocess.Popen(['adb', 'pull', '/sdcard/flatpaktransfer', f'/home/{username}/.flatpaktransfer'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = result.communicate()
            result.wait()
            if stdout == b"adb: error: failed to get feature set: no devices/emulators found\n":
                time.sleep(1) # give user time to connect phone
                continue
            if stderr:
                print("Error:", result.stderr)
                continue
            print(stdout.decode())
        except Exception as e:
            print("Unknown error:\n", e)
        print("Done transferring. Please disconnect your phone and clear the flatpaktransfer folder.")
        checkForFiles()
        time.sleep(5) # sleep for 5 seconds to wait for the phone to be disconnected

print("Ready. Running...")

waitForPhone()