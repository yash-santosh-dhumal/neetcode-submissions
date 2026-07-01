class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

     # Brute Force Approach

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
     # sorting approach 
        # nums.sort()
        # for i in range(len(nums)):
        #   if nums[i] == nums[i-1]:
        #       return True
        # return False        

      # Hashset Approach
        # seen = set()
        # for num in nums:
        #   if num in seen:
        #       return True 
        #   seen.add(num)
        # return False

      #Hashmap Length Approach
        return len(set(nums)) < len(nums)