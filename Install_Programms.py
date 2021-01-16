import os
import time

# Installing Programms
print("Installing programms now...")
time.sleep(1)
print("Installing Firefox now...")
os.system("choco install -y firefox")
print("Done!")
time.sleep(1)
print("Installing 7-Zip now...")
os.system("choco install -y 7zip")
print("Done!")
time.sleep(1)
print("Installing Discord now...")
os.system("choco install -y discord")
print("Done!")
time.sleep(1)
print("Installing Paint.NET now...")
os.system("choco install -y paint.net")
print("Done")
time.sleep(1)
print("Installing Steam now...")
os.system("choco install -y steam")
print("Done!")
time.sleep(1)
print("Installing Epic Games Launcher now...")
os.system("choco install -y epicgameslauncher")
print("Done!")
time.sleep(1)
print("Installing WhatsApp now...")
os.system("choco install -y whatsapp")
print("Done!")
time.sleep(1)
print("Installing OBS Studio now...")
os.system("choco install -y obs-studio")
print("Done!")
time.sleep(2)

# Installing optional programms
print("Installing optional programms now...")
time.sleep(1)

install_itunes = input("Do you want to install iTunes (Y/N)?")
time.sleep(1)
if install_itunes.lower() == "y":
    print("installing iTunes now...")
    time.sleep(1)
    os.system("choco install -y itunes")
else:
    print("Not installing iTunes.")
time.sleep(1)

install_zoom = input("Do you want to install Zoom (Y/N)?")
time.sleep(1)
if install_zoom.lower() == "y":
    print("installing Zoom now...")
    time.sleep(1)
    os.system("choco install -y zoom")
else:
    print("Not installing Zoom.")
time.sleep(1)

install_python = input("Do you want to install Python3 (Y/N)?")
time.sleep(1)
if install_python.lower() == "y":
    print("installing Python3 now...")
    time.sleep(1)
    os.system("choco install -y python3")
else:
    print("Not installing Python3")
time.sleep(1)

install_vsc = input("Do you want to install Visual Studio Code (Y/N)?")
time.sleep(1)
if install_vsc.lower() == "y":
    print("Installing Visual Studio Code now...")
    time.sleep(1)
    os.system("choco install -y vscode")
else:
    print("Not installing Visual Studio Code.")
time.sleep(1)

install_nodejs = input("Do you want to install Node.js (Y/N)?")
time.sleep(1)
if install_nodejs.lower() == "y":
    print("Installing Node.js now...")
    time.sleep(1)
    os.system("choco install -y nodejs")
else:
    print("Not installing Node.js.")
time.sleep(1)

install_win_terminal = input("Do you want to install Windows Terminal (Y/N)?")
time.sleep(1)
if install_win_terminal.lower() == "y":
    print("Installing Windows Terminal now...")
    time.sleep(1)
    os.system("choco install -y microsoft-windows-terminal")
else:
    print("Not installing Windows Terminal.")
time.sleep(1)

install_git = input("Do you want to install GIT (Y/N)?")
time.sleep(1)
if install_git.lower() == "y":
    print("Installing GIT now...")
    time.sleep(1)
    os.system("choco install -y git")
else:
    print("Not installing GIT.")
time.sleep(1)

install_blender = input("Do you want to install Blender (Y/N)?")
time.sleep(1)
if install_blender.lower() == "y":
    print("Installing Blender now...")
    time.sleep(1)
    os.system("choco install -y blender")
else:
    print("Not installing Blender.")
time.sleep(1)
