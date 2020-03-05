import redis
# connection
red = redis.Redis(host='localhost', port=6379, db=0)
# insert
def insert(key, value):
    try:
        red.set(str(key), str(value))
    except Exception as insert_error:
        print(insert_error)
    finally:
        print('added')
        red.close()
# read
def read():
    try:
        for key in sorted(red.scan_iter()):
            print(key, red.get(key))
    except Exception as read_error:
        print(read_error)
    finally:
        # print(red.get())
        red.close()
# update
def update(key, value):
    try:
        red.set(str(key), str(value))
    except Exception as insert_error:
        print(insert_error)
    finally:
        print('updated')
        red.close()
# delete
def delete(key):
    try:
       red.delete(key)
    except Exception as delete_error:
         print('deleted')
    finally:
        red.close()
# find
def find(key):
    try:
        available = red.get(key)
    except Exception as find_error:
        print(find_error)
    finally:
        print(available)

# call methouds
# insert data
# insert(4, "developer")
# update data
# update(1, 'designer')
# delete data
# delete(1)
# read data
# read()
# find data
find(5)


