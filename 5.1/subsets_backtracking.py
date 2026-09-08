"""
Experiment 5.1 - Problem 1: Subsets (LeetCode #78)
Approach: Backtracking
Subject: CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


def print_result(label, nums, result):
    print(f"{label}")
    print(f"  Input  : {nums}")
    print(f"  Count  : {len(result)}")
    print(f"  Output : {result}")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("  SUBSETS  |  Backtracking Approach")
    print("  LeetCode #78  |  Experiment 5.1")
    print("=" * 60)
    print()

    sol = Solution()

    tests = [
        [1, 2, 3],
        [0],
        [1, 2],
        [7],
        [4, 5, 6, 7],
    ]

    for t in tests:
        print_result(f"Test case nums = {t}", t, sol.subsets(t))

    print("=" * 60)
    print("  All test cases executed successfully.")
    print("=" * 60)
