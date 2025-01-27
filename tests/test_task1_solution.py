from calculator import *


def test_add():
    # test simple addition
    assert add(1, 2) == 3

    # test vector addition
    assert add([1, 2], [2, 3]) == [3, 5]


def test_multiply():
    # test simple multiplication
    assert multiply(2, 3) == 6

    # test vector scaling
    assert multiply(2, [1, 2, 3]) == [2, 4, 6]

    # test vector scaling (reverse)
    assert multiply([1, 2, 3], 2) == [2, 4, 6]

    # test scalar product
    assert multiply([1, 2, 3], [2, 3, 4]) == 2*1 + 2*3 + 3*4


def test_divide():
    assert divide(2, 3) == 2/3
