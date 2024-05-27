class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.main_index = 0
        self.sub_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.main_index < len(self.list_of_list):
            if self.sub_index < len(self.list_of_list[self.main_index]):
                item = self.list_of_list[self.main_index][self.sub_index]
                self.sub_index += 1
                return item
            self.main_index += 1
            self.sub_index = 0
        raise StopIteration

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()

flat_list = list(FlatIterator(list_of_list = [['dsd,sdfd'], [1,2,4,5]]))
print(flat_list)