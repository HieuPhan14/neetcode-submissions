class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.pick(nums, target, 0, {})

    def pick(self, nums, target, i, memo):
        key = (target, i)
        if key in memo:
            return memo[key]

        if i == len(nums):
            return [[]] if target == 0 else []

        if target < 0:
            return []

        first_number = nums[i]
        pick_first = self.pick(nums, target - first_number, i, memo)
        dont_pick_first = self.pick(nums, target, i + 1, memo)

        result = []
        for combination in pick_first:
            result.append([first_number, *combination])

        result += dont_pick_first

        memo[key] = result
        return result