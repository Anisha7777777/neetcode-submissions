class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashMap:
               return [hashMap[result], i]   
            hashMap[nums[i]] = i

        