import core.database as database
from core.database import db
from core.instagram import ig
from core.imgur import im
import time

"""The main function, basically does everything"""
db.createTabs()

"""
sub = "mytestsubgoaway"
accnt = "gins.e"
owner = "Aidgigi"
mode = "0"
newCon = db.createConnection(sub, accnt, owner, mode)
print(newCon)"""


def mainTesting():
    image = ig.getAndUpload(97774793)
    time.sleep(5)

    if image != False:
        print(image)

while True:
    mainTesting()
