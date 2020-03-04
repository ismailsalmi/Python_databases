from base64 import main
from pymongo import MongoClient

class Mongo():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['user']
    collection = db['students']
    # read methoud
    read = lambda self :self.collection.find({})
    # insert methoud
    insert = lambda self, name, lname: \
        self.collection.insert_one({"name":name, "lname": lname})
    # update methoud
    update = lambda self, name: self.collection.find_one_and_update(
        {"name":"ismail"}, {"$set":{"name": name}})
    # delete methoud
    delete = lambda self, name: \
        self.collection.find_one_and_delete({"name": name})


if __name__ == "__main__":
    mongo = Mongo()
    # read
    students = [student for student in mongo.read()]
    print(students[::-1])
    # inser
    # insert = mongo.insert('zouheir', 'salmi')
    # print(insert, 'is inserted')
    #update
    # update = mongo.update('samir')
    # print(update, 'is updated')
    # delete
    # delete = mongo.delete('samir')
    # print(delete , "is deleted")
    main()

