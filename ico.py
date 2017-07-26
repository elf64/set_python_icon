import os
import sys
import pip
import requests
from _winreg import *


def download():
    with open("page.png", "wb") as f:
        print "Downloading the Icon from {}".format(link)
        r = requests.get(
            link, stream=True
        )
        t_l = r.headers.get('content-length')
        if t_l is None:
            f.write(r.content)
        else:
            dl = 0
            t_l = int(t_l)
            for d in r.iter_content(chunk_size=4096):
                dl += len(d)
                f.write(d)
                done = int(50 * dl / t_l)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()


if __name__ == "__main__":
    # Install Pillow
    try:
        from PIL import Image
    except:
        print "Pillow not found!"
        print "Installing Pillow"
        pip.main(['install', 'Pillow'])

    link = "https://s24.postimg.org/xngee8e3p/page.png"
    if not os.path.exists('C:\\pyico'):
        os.makedirs('C:\\pyico')

    # Convert .png to .ico

    download()
    original = Image.open('page.png')
    original.save('C:\\pyico\\python.ico')
    os.remove("page.png")

    # Set the registry sub-key to the new icon

    keyVal = 'Python.File\\DefaultIcon'
    key = OpenKey(HKEY_CLASSES_ROOT, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key, "", 0, REG_SZ, "C:\\pyico\\python.ico")
    CloseKey(key)

    # Creating setico.bat which will refresh the icons

    with open('setico.bat', 'wb') as f:
        f.write("""
        @ECHO OFF
        SETLOCAL
        ie4uinit.exe -show
        DEL "%~f0"
        """)

    print "\nRun setico.bat to refresh the icons!!!"
