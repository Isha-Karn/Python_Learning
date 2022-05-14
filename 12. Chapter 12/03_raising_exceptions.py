def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError ("You have made a mistake!")

a= increment('hjhk45')
print (a)