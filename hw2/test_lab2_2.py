__author__ = 'BrianAguirre'

import unittest
from hw2_set import OurSet

class MySetTest(unittest.TestCase):

    def union_test(self, set1, set2):
        test_obj = OurSet()
        set1 = test_obj
        test_obj1 = OurSet()
        set2 = test_obj1

        item = 1
        assert (test_obj.add(item) == True)
    def intersection_test(self, set1, set2):
        test_obj = OurSet()
        set1 = test_obj
        test_obj1 = OurSet()
        set2 = test_obj1

        item = 1
        assert (test_obj.add(item) == True)

if __name__ == "__main__":
    test1 = OurSet()
    test2 = OurSet()
    unit_test = MySetTest()

    unit_test.intersection_test(test1, test2)
    unit_test.union_test(test1,test2)
