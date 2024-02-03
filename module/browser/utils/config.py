import os 
import time
path = os.getcwd() +'\chrome_driver\chromedriver.exe'
vpn_extension = os.getcwd() +'\chrome_driver\Vpn.crx' 
env = { "driver" : path,
        "vpn": vpn_extension }


