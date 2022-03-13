def two_sum(numbers: list[int], target: int) -> list[int]:
    """Two pointers solution: go from both ends till pointers met"""
    l, r = 0, 1
    while (numbers[l] + numbers[r]) != target:
        if numbers[l] + numbers[r] < target:
            if r < len(numbers) - 1:
                r += 1
            else:
                l += 1
                r = l + 1
    return [l + 1, r + 1]


if __name__ == '__main__':
    print(two_sum([2, 3, 4], 6))
    print(two_sum([-1, 0], -1))
    print(two_sum(
        [3, 24, 50, 79, 88, 150, 345], 200))
