class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        outcome = {}
        for i in range(len(nums)) :
            remain = target - nums[i]
            
            if remain in outcome :
                return [outcome[remain], i]
            else :
                outcome[nums[i]] = i
