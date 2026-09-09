class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.pick(nums, target, 0)

    def pick(self, nums: List[int], target: int, i: int) -> List[List[int]]:
        if i == len(nums):
            if target == 0:
                return [[]]
            else: return []

        if target < 0:
            return []

        first_number = nums[i]
        pick_first_number = self.pick(nums, target - first_number, i)
        dont_pick_first = self.pick(nums, target, i + 1)

        result = []
        for combination in pick_first_number:
            true_comb = [first_number, *combination]
            result.append(true_comb)

        result += dont_pick_first
        return result