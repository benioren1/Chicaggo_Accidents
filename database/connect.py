from pymongo import MongoClient
from database.config import *

client = MongoClient(CLIENT)

Chicago_db = client[DATABASE]

Accidents = Chicago_db['Accidents']

Location = Chicago_db['Location']

Injuries = Chicago_db['Injuries']

Dates =Chicago_db['Dates']
