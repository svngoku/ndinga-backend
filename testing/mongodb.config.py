import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NDINGA"]
mycol = mydb["ki_fr"]

def getAll(mycol):
    for x in mycol.find():
        print(x)

getAll(mycol)