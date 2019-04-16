from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.FormData

// Insertion of Data

db.RichCounts.insert_one(
        {
            # "ID": db.form.count() + 1,
            "l1": 0,
            "l2": 0,
            "l3": 0,
            "l4": 0,
            "l5": 0,
            "r1": 0,
            "r2": 0,
            "r3": 0,
            "r4": 0,
            "r5": 0,

        }
        )       

// Retrieving

a = db.RichCounts.find()
print(a[0]['l1'])  // for rich count of l1        