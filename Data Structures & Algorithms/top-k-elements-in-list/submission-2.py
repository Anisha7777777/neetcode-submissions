class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num]+=1
        frequency = sorted(hashmap, key = hashmap.get , reverse = True)

        return frequency[:k]