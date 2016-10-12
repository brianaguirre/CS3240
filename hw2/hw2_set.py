__author__ = 'BrianAguirre'

#Global Method: Tests if item is present in list
def is_present(x, list1):
        found = False
        for i in range(0, len(list1)):
            if (list1[i] == x):
                found = True
        return found


class OurSet(object):

    """
    __init__(self)
    This constructor is used to initialize an empty set.
    """

    def __init__(self):
        self.data = []
        self.name = "Brian"

    """
    add(self, item)
    If the parameter to this method is not already in the set object, add it to the set.  Return True or False to indicate if the item was added to the set.
    """

    #is_present() METHOD FOR ADD:

    def add(self, item):
        list2 = []
        if (is_present(item, self.data) == True):
            return False
        else:
            (self.data).append(item)
            return True

    """
    addList(self, list)
    Add each item in the list to the set, unless it already is in the set. Return True if any item was added the set, otherwise False.
    """
    def add_list(self, list1):
        added = False
        for i in range (0, len(list1)):
            if (is_present(list1[i], self.data) == False):
                self.data.append(list1[i])
                added = True

        return added

    """
    __str__(self)
    Return a string representation of the set, in a format like this:  <2, 5, 7, 11>
    where the contents of the set are surrounded by "angle-brackets" and each item is separated by a comma and exactly one space.
    """

    def __str__(self):
        string_data = "<"
        length = len(self.data)
        for i in range (0, length):
            if (i<length-1):
                string_data  = string_data + str(self.data[i]) + ", "
            elif (i == length-1):
                string_data = string_data + str(self.data[i]) + ">"

        return string_data
    """
    __len__(self)
    Returns the number of items in the set object.
    """
    def __len__(self):
        return len(self.data)

    """
    __iter__(self)
    To allow you to use in and not in to process items in an OurSet object, you need to define this method. In our case, you just need to know that an iterator is defined for the list inside your set object, so you can just do something with that.  It's simple, just one line of code!
    """

    def __iter__(self):
        return self.data.__iter__()

    """
    union(self, set2)
    Carry out a set-union operation between the current set object and the parameter. Return the union as the return value. Do not modify the current set object or the parameter.    (Note:  you don't have to do this for this homework, but the nice way to do this would be to define the __add__(self, other) method so you could just use the + operator to do a union!)
    """
    def union(self, set2):
        union_set = OurSet()
        for i in range(0, len(self.data)):
            if (is_present(self.data[i], union_set.data) == False):
                union_set.data.append(self.data[i])
        for j in range (0, len(set2.data)):
            if (is_present(set2.data[j], union_set.data) == False):
                union_set.data.append(set2.data[j])

        return union_set

    """"
    intersection(self, set2)
    Carry out a set-intersection operation between the current set object and the parameter.  Return the intersection as the return value. Do not modify the current set object or the parameter.
    """
    def intersection(self, set2):
        inter_set = OurSet()
        for i in range(0, len(self.data)):
            if (is_present(self.data[i], inter_set.data) == False and is_present(self.data[i], set2.data) == True):
                inter_set.data.append(self.data[i])

        return inter_set

if __name__ == "__main__":
    pass