
ZERO: str = '0'


def task(array: str) -> int:
    def _counting(__data, __left, __right):
        if __right <= __left:
            return -1
        __middle = (__left + __right) // 2
        if __data[__middle] == ZERO and (
                __middle == 0 or ZERO != __data[__middle - 1]):
            return __middle
        elif __data[__middle] == ZERO:
            return _counting(__data, __left, __middle)
        return _counting(__data, __middle + 1, __right)
    return _counting(list(array), 0, len(array))


if __name__ == '__main__':
    print(task('111111111000000'))
