@echo off
set ICON_FILE=C:\Users\Abeled\Desktop\AMIC\numpsoft.ico
py -m PyInstaller --onefile --icon=%ICON_FILE% -w index.py
