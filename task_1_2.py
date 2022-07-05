
def overlap(first_a: int, second_a: int, first_b: int, second_b: int) -> int:
    max_a = max(first_a, second_a)
    max_b = max(first_b, second_b)
    min_a = min(first_a, first_b)
    min_b = min(first_b, second_b)
    if min_a >= max_b or max_a <= min_b:
        return 0
    elif min_a <= min_b <= max_b <= max_a:
        return max_b - min_b
    elif min_b <= min_a <= max_a <= max_b:
        return max_a - min_a
    elif min_b <= min_a <= max_b:
        return max_b - min_a
    return max_a - min_b


def task(
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        x3: int,
        y3: int,
        x4: int,
        y4: int
) -> int:
    overlapping_x = overlap(x1, x2, x3, x4)
    overlapping_y = overlap(y1, y2, y3, y4)
    return overlapping_x * overlapping_y


if __name__ == '__main__':
    print(task(1, 1, 2, 2, 3, 3, 4, 4) or False)
