#strategy design pattern example

class SortStrategy:
    def sort(self, data):
        raise NotImplementedError

class QuickSort(SortStrategy):
    def sort(self, data):
        print('Quick sort')

class MergeSort(SortStrategy):
    def sort(self, data):
        print('Merge sort')

class Sorter:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def sort(self, data):
        self.sort_strategy.sort(data)

if __name__ == '__main__':
    quick = QuickSort()
    merge = MergeSort()

    sorter = Sorter(quick)

    sorter.sort([1, 2, 3, 4, 5])

    sorter.sort_strategy = merge

    sorter.sort([1, 2, 3, 4, 5])