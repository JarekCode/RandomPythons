# -------
# PyMongo
# -------
# this code uses 'pymongo' to communicate with a mongo database

# import
import pymongo

# -----------
# mongo setup
# -----------
# setting up the client
mongoClient = pymongo.MongoClient()
# specifying the database = 'myEpicDB'
myEpicDB = mongoClient.myEpicDB

# ----
# find
# ----
# return all documents from 'myEpicCollection' collection
allDocuments = myEpicDB.myEpicCollection.find()

# ------
# insert
# ------
# Move the Document(scheduledJob) into the archivedJobs Collection

for document in allDocuments:
    myEpicDB.newCollection.insert_one(document)

# ------
# delete
#-------
# Delete the Document(scheduledJob) from scheduledJobs Collection

for document in allDocuments:
    myEpicDB.myEpicCollection.delete_one(document)

# ------
# update
# ------
# update a document in 'myEpicCollection' with a specific _id
idVariable = "123abc4477"

myID = { "_id" : idVariable }
myValue = { "$set" : { "status" : "running" } }

myEpicDB.myEpicCollection.update_one(myID, myValue)

# -------------------------
# remove element from array
# -------------------------
# remove a specific element from an array in a document from 'myEpicCollection' with a specific _id
idVariable = "456def4477"
itemToRemove = 4477

myID = { "_id" : document['_id'] }
myValue = { "$pull" : { "listOfNumbers" : itemToRemove } }

myEpicDB.myEpicCollection.update_one(myQuery, newValues)

# ------------------------
# closing mongo connection
# ------------------------
mongoClient.close()
