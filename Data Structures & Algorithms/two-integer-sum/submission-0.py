class Solution:
    #two nested approach
     def twoSum(self, nums: List[int], target: int) -> List[int]:
     #     for i in range(len(nums)):
     #         for j in range(i+1,len(nums)):
     #             if nums[i] + nums[j] == target:
     #                 return [i,j]
     #     return []      
    
    # Hashmap 2 pass approach
    # hashmap = {}
    # for i,n in enumerate(nums):
    #    hashmap[n]=i

    # for i,n in enumerate(nums):
    #    diff= target - n
    #    if diff in hashmap and hashmap[diff] !=i:
    #         return ([i,hashmap[diff]])
    # return []

    # hashmap one pass approach
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]= i