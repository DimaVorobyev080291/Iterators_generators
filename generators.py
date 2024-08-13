import types

def flat_generator(list_of_lists):
        """Генератор возвращает элементы из списка списков с двойным уровнем вложености"""
        for sub_list in list_of_lists:
            for elem in sub_list:
                yield elem


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()


def flat_generator_difficult(list_of_list):
    """Генератор возвращает элементы из списка списков с любым уровнем вложености"""
    for elem in list_of_list:
        if isinstance(elem, list): 
            for sub_elem in flat_generator_difficult(elem):  
                yield sub_elem
        else:
            yield elem


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_difficult(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator_difficult(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_difficult(list_of_lists_2), types.GeneratorType)

if __name__ == '__main__':
    test_4()