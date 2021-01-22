import unittest
from unittest import TestCase
import random

from sorting.sorting import SelectionSort, InsertionSort

class TestBaseSort(TestCase):
    def is_sorted(self, lst):
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i+1]:
                return False

        return True


class TestSortingClass(TestBaseSort, TestCase):
    def setUp(self):
        self.SORTED_LIST = [x for x in range(0,10)]
        self.REVERSE_SORTED_LIST = [x for x in range(9,-1,-1)]

        self.RANDOM_LIST = []
        for _ in range(0,10):
            n = random.randint(1,10)
            self.RANDOM_LIST.append(n)

    def test_selection_sort(self):
        self._test_sort_class(SelectionSort)
    
    def test_insertion_sort(self):
        self._test_sort_class(InsertionSort)
        
    def _test_sort_class(self, sort_class):
        sort_class.sort(self.SORTED_LIST)
        self.assertTrue(self.is_sorted(self.SORTED_LIST))

        sort_class.sort(self.REVERSE_SORTED_LIST)
        self.assertTrue(self.is_sorted(self.REVERSE_SORTED_LIST))

        sort_class.sort(self.RANDOM_LIST)
        self.assertTrue(self.is_sorted(self.RANDOM_LIST))


if __name__ == '__main__':
    unittest.main()