# AlpineQuest-appium-pytest

# Setaps
This project is designed to facilitate automated testing of QT Android applications using the Appium framework with Python.

## Prerequisites
Before you begin, ensure you have met the following requirements:

* Python3 installed on your system.
* Android Studio installed
* Appium server installed and configured 
* Appium inspector installed and configured
* Android SDK and platform tools installed
* PyCharm Community Edition installed.

## Installation for Ubuntu
#### Step 1 : Install Java in your system.

```sh
  sudo apt update
  ```
```sh
  sudo apt install openjdk-11-jdk
  ```
```sh
  sudo apt install openjdk-11-jdk
  ```
```sh
  java -version
  ```
#### Step 2 : – Install Android Studio in your system.apt update
  * Open “ubuntu software” application in your system.
  * Search “Android Studio”.
  ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/511074b8-abbc-4b43-858a-7c5fae946a42)
  * Select the first one and click on “Install” button.
  * Follow the instructions described in the settings <a href="https://aurigait.com/blog/how-to-setup-appium-in-ubuntu/">link</a>.

#### Step 3 :- Installing appium desktop 
 * <a href="https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4">Release v1.22.3-4 · appium/appium-desktop · GitHub</a> -> go to this site and download the Appium-server-GUI -linux AppImage
   
#### Step 4 :- Installing appium inspector.
 * <a href="https://github.com/appium/appium-inspector/releases">Releases · appium/appium-inspector · GitHub</a> -> go to this site and download the Appium-Inspector-GUI- linux AppImage.

#### Step 5 :- Set up the environment variables in the bash file.
  * Open the terminal (ctrl + alt + t)
  * Run this command :-
    ```sh
      vim .bashrc
      ```
  * At the end of the page, add all these below variables with their path and save
    ```sh
        export ANDROID_HOME=~/Android/Sdk
        export PATH=$PATH:$ANDROID_HOME/tools
        export PATH=$PATH:$JAVA_HOME/bin
        export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
      ```


## Usage
* Run Android Studio
    - [ ]  Create device
          ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/ca159520-495b-49d5-881f-bd9b069fe8eb)
* Run Appium
    - [ ] Go to Appium Server GUI -> Advanced
    - [ ] Server address: localhost
    - [ ] Port: 4723
    - [ ] Allow CORP: yes
          
       ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/4778b9b0-ae09-4785-a0fb-219ce6c82285)

* Run Appium Inspector
    - [ ] Remote host: localhost
    - [ ] Port: 4723
    - [ ] Path: /wd/hub
    - [ ] Allow Unauthorized Certificates
        - [ ]  list devices
  ```sh
    adb .devices
    ```
    - [ ] Select your capabilities
    - [ ] Start server
          
  ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/c093fb3f-72df-4321-aeed-ebc1b5478d3d)

  * Open PyCharm Community Edition
    ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/d440ce49-d4cf-4678-8aca-769b55e17d96)

      - [ ] File --> New Project
  
