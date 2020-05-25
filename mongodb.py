#functions and libraries
from pymongo import MongoClient
from pprint import pprint
#config
client = MongoClient("mongodb+srv://hachi:1234abcd@cluster0-yh2mp.mongodb.net/test?retryWrites=true&w=majority")
db=client.test
#user functions

def insertComment(comment):
    db.comments.insert_one(comment)