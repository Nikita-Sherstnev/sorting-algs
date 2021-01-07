class SelectionSort():
    def sort(self, lst):
        for i in range(0, len(lst)):
            min = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min]:
                    min = j
            
            lst[i], lst[min] = lst[min], lst[i]


class InsertionSort():
    def sort(self, lst):
        for i in range(1, len(lst)):
            j = i
            while j > 0 and lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j-=1
