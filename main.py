import sys
import os
import time

# Installing Chocolatey
print("Getting your install ready...\n")
# os.system(
#    "powershell -Command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
print("\nInstall ready!")
time.sleep(1)

# Installing Programms
print("\nInstalling programms now...")
time.sleep(1)
print("Installing Chrome now...")
os.system('powershell -Command $Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "http: // dl.google.com/chrome/install/375.126/chrome_installer.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent / install" -Verb RunAs -Wait; Remove-Item $Path\$Installer')
print("Done!")
time.sleep(1)
print("Installing Firefox now...")
os.system("choco install firefox")
print("Done!")
time.sleep(1)
print("Installing 7-Zip now...")
os.system("choco install 7zip")
print("Done!")
time.sleep(1)
print("Installing Discord now...")
os.system("choco install discord")
print("Done!")
time.sleep(1)
print("Installing Paint.NET now...")
os.system("choco install paint.net")
print("Done")
time.sleep(1)
print("Installing Steam now...")
os.system("choc install steam")
print("Done!")
time.sleep(1)
print("Installing Epic Games Launcher now...")
os.system("choco install epicgameslauncher")
print("Done!")
time.sleep(1)
print("Installing WhatsApp now...")
os.system("choco install whatsapp")
print("Done!")
time.sleep(1)
print("Installing OBS Studio now...")
os.system("choco install obs-studio")
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
    os.system("choco install itunes")
else:
    print("Not installing iTunes.")
time.sleep(1)

install_zoom = input("Do you want to install Zoom (Y/N)?")
time.sleep(1)
if install_zoom.lower() == "y":
    print("installing Zoom now...")
    time.sleep(1)
    os.system("choco install zoom")
else:
    print("Not installing Zoom.")
time.sleep(1)

install_python = input("Do you want to install Python3 (Y/N)?")
time.sleep(1)
if install_python.lower() == "y":
    print("installing Python3 now...")
    time.sleep(1)
    os.system("choco install python3")
else:
    print("Not installing Python3")
time.sleep(1)

install_vsc = input("Do you want to install Visual Studio Code (Y/N)?")
time.sleep(1)
if install_vsc.lower() == "y":
    print("Installing Visual Studio Code now...")
    time.sleep(1)
    os.system("choco install vscode")
else:
    print("Not installing Visual Studio Code.")
time.sleep(1)

install_nodejs = input("Do you want to install Node.js (Y/N)?")
time.sleep(1)
if install_nodejs.lower() == "y":
    print("Installing Node.js now...")
    time.sleep(1)
    os.system("choco install nodejs")
else:
    print("Not installing Node.js.")
time.sleep(1)

install_win_terminal = input("Do you want to install Windows Terminal (Y/N)?")
time.sleep(1)
if install_win_terminal.lower() == "y":
    print("Installing Windows Terminal now...")
    time.sleep(1)
    os.system("choco install microsoft-windows-terminal")
else:
    print("Not installing Windows Terminal.")
time.sleep(1)

install_git = input("Do you want to install GIT (Y/N)?")
time.sleep(1)
if install_git.lower() == "y":
    print("Installing GIT now...")
    time.sleep(1)
    os.system("choco install git")
else:
    print("Not installing GIT.")
time.sleep(1)

install_blender = input("Do you want to install Blender (Y/N)?")
time.sleep(1)
if install_blender.lower() == "y":
    print("Installing Blender now...")
    time.sleep(1)
    os.system("choco install blender")
else:
    print("Not installing Blender.")
time.sleep(1)
