import core.database as database
from core.database import db
import time

"""The main function, basically does everything"""
db.createTabs()

sub = "mytestsubgoaway"
accnt = "salad.snake"
owner = "Aidgigi"
mode = "0"
newCon = db.createConnection(sub, accnt, owner, mode)
print(newCon)
