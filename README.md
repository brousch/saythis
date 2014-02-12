# Say This #

An Android or Desktop app that uses your platform's text to speech engine 
to speak what you've typed. This project is developed with Kivy and Plyer. 
It can be compiled for Android using python-for-android and buildozer.


## Running ##

### Windows ###

1. Install espeak - http://espeak.sourceforge.net/
2. Clone this repository
3. Install Kivy - http://kivy.org/#download
4. Run kivy.bat
5. `pip install plyer`
6. `python saythis\main.py`

### OSX ###

1. Clone this repository
2. Install Kivy - http://kivy.org/#download
3. `pip install plyer`
4. `kivy saythis/main.py`

### Linux ###

1. Install espeak or flite from your distro's repositories
2. Clone this repository
3. Install Kivy - http://kivy.org/#download
4. `pip install plyer`
5. `python saythis/main.py`

### Android ###

1. Install from Google Play or Amazon App Store

## Compiling an APK ##

1. Install buildozer - https://github.com/kivy/buildozer
2. `buildozer android debug`



