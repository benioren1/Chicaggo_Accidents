from pymongo import MongoClient
from database.config import *

client = MongoClient(CLIENT)

Chicago_db = client[DATABASE]

Accidents = Chicago_db['Accidents']



