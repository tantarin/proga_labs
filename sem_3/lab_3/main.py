from typing import List

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8


def two_sum(nums: List[int], target: int) -> tuple[int, ...]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return i, hashmap[complement]


if __name__ == "__main__":
    assert two_sum(lst, target) == (0, 6), "Базовый тестовый набор (test case)"
    assert two_sum([1, 1, 2, 3], 2) == (0, 1), "test case #2"
    assert two_sum(list(range(1000000)), 999999) == (0, 999999)
