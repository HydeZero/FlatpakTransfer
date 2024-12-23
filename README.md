# FlatpakTransfer

## What is it?

This is a program designed to copy .flatpakref files from a phone to your computer and install them. This is a simple program using python.

## Requirements

You need:

* An android phone (iOS won't work)
* Developer options turned on with said android phone.
* Android debug bridge
* An internet connection
* A cable to connect your phone to your computer

### Getting the software needed

Install adb via apt on Ubuntu or Debian-based distributions.

```bash
sudo apt install adb
```

For other platforms, get it from [developer.android.com](https://developer.android.com/tools/releases/platform-tools). Download the linux zip file and extract it to /opt for system-wide usage, via:

```bash
sudo unzip platform-tools-latest-linux.zip -d /opt
```

If you want to uninstall it, just `rm` the created directory (platform-tools).

***BE VERY CAREFUL WHEN RUNNING THIS COMMAND, A TYPO CAN MESS YOUR SYSTEM UP***

```bash
sudo rm -r /opt/platform-tools # always double check this directory before running the command
```

### Enabling USB Debugging on your phone

1. Open settings and look for developer settings. If that option is avaliable, skip to step 5.
2. Go to About Phone --> Software information (on Samsung, software information may be located in another location on other phones)
3. Tap "Build Number" until you are asked for your screen lock. Unlock it, and you will become a developer.
4. Exit out of About Phone.
5. Enter Developer Settings.
6. Enable the toggle for "USB Debugging"

## Usage

Just run the program after cloning the repository.

```bash
git clone https://github.com/HydeZero/FlatpakTransfer.git && cd FlatpakTransfer
python3 ./src/main.py
```

Plug your phone in, and it may ask to verify the computer's RSA fingerprint. Check the option for "Always trust" if you want to avoid this pop up every time, then unplug the phone.

On your phone, go to [Flathub](https://flathub.org/) and download flatpak refs using the "Install" button. Move any downloaded flatpakref files to "flatpaktransfer" at the root of your phone. You may need to make this folder.

Plug your phone in when the program is running. It should automatically pull the files from the device and install the flatpak software.

When you see the message "Done transferring. Please disconnect your phone and clear the flatpaktransfer folder," you are done. Unplug your phone within 5 seconds and delete the files within the flatpaktransfer folder on your phone.