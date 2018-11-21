import pymongo
from pymongo import MongoClient

conn = MongoClient('127.0.0.1')
db = conn['myDB']
collection = db['language']

#Creating a collection
db.language.insert({"id": "1", "name": "C", "grade":"Boring"})
db.language.insert({"id": "2", "name":"Python", "grade":"Interesting"})
db.language.insert({"id": "3", "name":"Ruby", "grade":"Awesome"})
db.language.insert({"id": "4", "name":"Scala", "grade":"Boring"})
db.language.insert({"id": "5", "name":"Java", "grade":"Interesting"})
db.language.insert({"id": "6", "name":"C#", "grade":"Awesome"})
db.language.insert({"id": "7", "name":"Pascal", "grade":"Awesome"})
db.language.insert({"id": "8", "name":"HTML", "grade":"Interesting"})
db.language.insert({"id": "9", "name":"Haskell", "grade":"Boring"})
db.language.insert({"id": "10", "name":"Javascript", "grade":"Awesome"})

#Reading it
print("After create\n",list(db.language.find()))

#Updating the collection
db.language.update({"name":"C"}, {"$set":{"grade":"Yay"}})
print("After update\n",list(db.language.find()))

#Deleting the collection
#db.language.drop()
#print("After delete\n", list(db.language.find()))