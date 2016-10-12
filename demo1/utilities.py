__author__ = 'BrianAguirre'

def remove_dupes(the_list):
    res = []
    for item in the_list:
        if not item in res:
            res.append(item)
    return res


#PRINT LINE BELOW: will get printed since all code is imported and executed.
print ("Testing file under utilities.py")

#To stop utilities from running EVERYTHING in it:
#add a if __name__ = "__main__": statement such that:

