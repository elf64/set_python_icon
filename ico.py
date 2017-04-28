import os
import pip
import urllib
from _winreg import *
# Install Pillow
try:
	from PIL import Image
except:
	print "Pillow not found!"
	print "Installing Pillow"
	pip.main(['install', 'Pillow'])
# Download the image
png_to_ico = urllib.URLopener()
png_to_ico.retrieve("https://s24.postimg.org/xngee8e3p/page.png",
					"page.png")
# Create folder for .ico
if not os.path.exists('C:\\pyico'):
	os.makedirs('C:\\pyico')
# Convert .png to .ico
original = Image.open('page.png')
original.save('C:\\pyico\\python.ico')
# Set the registry sub-key to the new icon
keyVal = 'Python.File\\DefaultIcon'
key = OpenKey(HKEY_CLASSES_ROOT, keyVal, 0, KEY_ALL_ACCESS)
SetValueEx(key, "", 0, REG_SZ, "C:\pyico\python.ico")
CloseKey(key)
# Remove the page.png file
os.remove("page.png")
# Creating setico.bat which will refresh the icons
with open('setico.bat', 'w') as f:
	f.write('ie4uinit.exe -show\nexit')
print "Run setico.bat to refresh the icons!!!"
