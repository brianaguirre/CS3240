__author__ = 'BrianAguirre'

from hw2_set import OurSet

test = OurSet()
test2 = OurSet()

if __name__ == "__main__":
    test.add(32413)
    print(test.add("Brian"))
    print(test.add("Brian"))
    test.add("Helen")
    test.add(123)
    test.add_list([1, 2, 5, 3, 4, 5])

    test2.add_list([1, 5, 3, 2, 2, 5, 2, 6, 7, 8])

    print(str(test))
    print(len(test))
    print(iter(test))
    print(test.union(test2))
    print(test.intersection(test2))

