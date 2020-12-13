from pymongo import MongoClient

client=MongoClient("Host","port","username","password")
db=client["db_name"]
collection=db["coll_name"]
collection.find_one({"name":"Sumit"})
client.close()