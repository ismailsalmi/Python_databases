from base64 import main
from pyrebase import initialize_app

class Firebase:
    # firebase connection
   config = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "storageBucket": ""
    }

   firebase = initialize_app(config)
   db = firebase.database()
   users = db.child("users")
   # insert
   insert = lambda self,username, name, lname, age: self.users.child(
       username).set({"name": name, "lname": lname, "age": age})
   # update
   update = lambda self,username, name, lname, age: self.users.child(
       username).update({"name": name,"lname": lname, "age": age})
   # delete
   delete = lambda self, username: self.users.child(username).remove()
   # read
   read = lambda self: self.users.get()
if __name__=="__main__":
    firebase = Firebase()
    # insert
    # insert = firebase.insert(username='hnsgf3', name='ismail', lname='salmi', age=24)
    # print(insert, 'inserted')
    # update
    # update = firebase.update(username='qlmys1', name='samir', lname='salmi', age=24)
    # print(update, 'updated')
    # delete
    # delete = firebase.delete(username='hnsgf3')
    # is_deleted = 'Deleted' if delete else 'Not deleted'
    # print(is_deleted)
    # read
    read = firebase.read().each()
    for user in read:
        print(user.val()['name'])
    main()


