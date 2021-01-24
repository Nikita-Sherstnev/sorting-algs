class SelectionSort():
    @staticmethod
    def sort(lst):
        for i in range(0, len(lst)):
            min = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min]:
                    min = j
            
            lst[i], lst[min] = lst[min], lst[i]


class InsertionSort():
    @staticmethod
    def sort(lst):
        for i in range(1, len(lst)):
            j = i
            while j > 0 and lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j-=1


class Shellsort():
    @staticmethod
    def sort(lst):
        h = 1
        while h < len(lst)//3:
            h = 3*h + 1
        while h >= 1:
            for i in range(h, len(lst)):
                j = i
                while j >= h and lst[j] < lst[j-h]:
                    lst[j], lst[j-h] = lst[j-h], lst[j]
                    j -= h
            h = h//3

