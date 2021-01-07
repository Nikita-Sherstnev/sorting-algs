import unittest
from unittest import TestCase
import random

from sorting.sorting import SelectionSort, InsertionSort

class TestBaseSort(TestCase):
    def isSorted(self, lst):
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i+1]:
                return False

        return True


class TestSelectionSort(TestBaseSort, TestCase):
    def setUp(self):
        self.SORTED_LIST = [x for x in range(0,10)]
        self.REVERSE_SORTED_LIST = [x for x in range(9,-1,-1)]

        self.RANDOM_LIST = []
        for i in range(0,10):
            n = random.randint(1,10)
            self.RANDOM_LIST.append(n)

        self.sort_class = SelectionSort()

    def test_sorted_list_is_sorted(self):
        self.sort_class.sort(self.SORTED_LIST)
        self.assertTrue(self.isSorted(self.SORTED_LIST))

    def test_reverse_sorted_list_is_sorted(self):
        self.sort_class.sort(self.REVERSE_SORTED_LIST)
        self.assertTrue(self.isSorted(self.REVERSE_SORTED_LIST))

    def test_random_list_is_sorted(self):
        self.sort_class.sort(self.RANDOM_LIST)
        self.assertTrue(self.isSorted(self.RANDOM_LIST))



if __name__ == '__main__':
    unittest.main()