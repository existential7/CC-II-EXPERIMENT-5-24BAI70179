"""
Experiment 5.2 - Problem 2: Combination Sum (LeetCode #39)
Approach: Backtracking with start index (reuse allowed)
Subject: CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    current.append(candidates[i])
                    backtrack(i, current, remaining - candidates[i])
                    current.pop()

        backtrack(0, [], target)
        return result


def print_result(candidates, target, result):
    print(f"Test case candidates = {candidates}, target = {target}")
    print(f"  Count  : {len(result)}")
    print(f"  Output : {result}")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("  COMBINATION SUM  |  Backtracking Approach")
    print("  LeetCode #39  |  Experiment 5.2")
    print("=" * 60)
    print()

    sol = Solution()

    cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
        ([3, 5], 8),
        ([2, 4], 6),
        ([2, 3], 6),
    ]

    for cand, tgt in cases:
        print_result(cand, tgt, sol.combinationSum(cand, tgt))

    print("=" * 60)
    print("  All test cases executed successfully.")
    print("=" * 60)
