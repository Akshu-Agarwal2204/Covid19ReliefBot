import os
os.system("pip3 install -r requirements.txt")

from bot import client
VERSION = "0.0.1"
client.run(VERSION)