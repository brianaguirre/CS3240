__author__ = 'BrianAguirre'

"""
maxmin(list)
Assume the parameter is a any valid list containing comparable values of the same type. Return a tuple where the first value is the maximum value found in the list (based on the > operator) and the second value in the tuple is the minimum value found in the list (based on the < operator).  If the list is empty, return the special Python value None.  Examples:
For the list [1, 3, 3], return (3, 1)
For the list [3, 1, -2], return (3, -2)
For the list ['Q', 'Z', 'C', 'A'], return ('Z', 'A')
Note: Constraint for this homework: do not use the built-in Python methods max() or min() for this. You cannot sort the list either.
"""

def maxmin(list1):
    max_num = 0
    min_num = 0
    if len(list1) == 0:
        return None
    else:
        max_num = list1[0]
        min_num = list1[0]
        for i in range(0, len(list1)):
            if list1[i] > max_num:
                max_num = list1[i]
            if list1[i] < min_num:
                min_num = list1[i]
        return "(" + str(max_num) + "," + str(min_num) + ")"



#SIMPLE TEST
#print(maxmin([1, 4, 2, 3, 532, 1]))


"""
common_items(list1, list2)
Assume that list1 and list2 are valid lists.  Return a list that contains items that are found in both lists.  If there are no such common items, return an empty list.  The list returned will not contain any duplicate items.
Note: Constraint for this homework: do not use the built-in Python support for sets for this.
"""
def is_present(x, list1):
    present = False
    length = len(list1)
    for i in range(0, length):
        if (list1[i] == x):
            present = True

    return present


def common_items(list1, list2):
    temp_item = None
    common_list = []
    if (len(list1) == 0 or len(list2) == 0):
        return None
    else:
        length1 = len(list1)
        length2 = len(list2)
        for i in range (0, length1):
            temp_item = list1[i]
            for j in range (0, length2):
                if (list1[i] == list2[j] and is_present(temp_item, common_list) == False):
                    common_list.append(list1[i])
    return common_list


#SIMPLE TEST
#print(common_items([1, 4, 2, 3, 532, 1],[4321, 4, 5, 1, 532, 1]))

"""
notcommon_items(list1, list2)
Assume that list1 and list2 are valid lists. Return a list that contains items that only occur in one of list1 or list2 (i.e. not in both lists). The list returned will not contain any duplicate items.
Note: Constraint for this homework: do not use the built-in Python support for sets for this.
"""

def notcommon_items(list1, list2):
    temp_item = None
    notcommon_list = []
    if (len(list1) == 0 and len(list2) == 0):
        return None
    elif (len(list1) == 0 and len(list2) > 0):
        return list2
    elif (len(list1) > 0 and len(list2) == 0):
        return list1
    else:
        length1 = len(list1)
        length2 = len(list2)
        for i in range (0, length1):
            temp_item = list1[i]
            for j in range (0, length2):
                if (is_present(temp_item, list2) == False and is_present(temp_item, notcommon_list) == False):
                    notcommon_list.append(list1[i])
    return notcommon_list


#SIMPLE TEST
#print(notcommon_items([1, 4, 2, 3, 532, 1],[4321, 4, 5, 1, 532, 1]))

"""
count_list_items(list)
Assume the parameter is a valid list that may contain duplicate items.  Return a dictionary that stores counts of how often each item occurs, i.e. each key in the dictionary will be a unique item from the list, and that key's value will be how often it occurs in the list.  Example:
For the list [1, 3, 2, 2, 3, 1, 1, 2], the dictionary returned would contain {1: 3, 2: 3, 3: 2}
"""

def count_list_items(list1):
    count_dic = {}
    length = len(list1)
    if (length == 0):
        return None
    elif (length == 1):
        count_dic = {list1[0]: 1}
        return count_dic
    else:
        for i in range (0, length):
            temp = list1[i]
            count = 0
            for j in range (0, length):
                if (temp == list1[j]):
                    count+=1
            count_dic[temp] = count
        return count_dic

#SIMPLE TEST
#print(count_list_items([1, 4, 2, 3, 532, 1]))

if __name__ == "__main__":
    pass
