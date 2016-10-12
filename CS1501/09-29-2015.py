__author__ = 'BrianAguirre'

#Interview Problems

def min_value(list1):
    l = len(list1)
    head = list1[0]
    tail = list1[l-1]

    if l == 1:
        return list1[0]

    else:
        if head < tail:
            return head

        else:
            average = int((head + tail)/2)
            middle = list1[int(l/2)]

            if average < middle:
                new_list = list1[int(l/2):]
                return min_value(new_list)
            else:
                new_list = list1[1:int(l/2)+1]
                return min_value(new_list)

def backwards(msg):
    list1 = []
    word = ""
    for i in range (0, len(msg)):
        if (msg[i] == " "):
            list1.append(word)
            word = ""

        else:
            word = word + msg[i]

    sentence = ""
    for i in reversed(list1):
        sentence += i + " "

    print(sentence)
