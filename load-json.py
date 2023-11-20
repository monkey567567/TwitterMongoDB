import json
from pymongo import MongoClient
import sys


#perhaps a try execepy block here
client = MongoClient('mongodb://localhost:{}'.format(sys.argv[2]))

db = client["291db"]
tweetscollection = db["tweets"]

tweetscollection.delete_many({})

json_file = sys.argv[1]



with open(json_file, "r") as file:
    data = json.load(file)
    
tweets = data["tweets"]
tweetscollection.insert_many(tweets)

