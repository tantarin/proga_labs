from typing import List


def two_sum(nums: List[int], target: int) -> tuple[int, ...]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return i, hashmap[complement]