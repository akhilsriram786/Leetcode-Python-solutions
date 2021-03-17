class Solution:
    def check(self, nums: List[int]) -> bool:
        
        numsSorted = sorted(nums)

        # iterate over all list elements
        for i in range(len(nums)):
          # check every rotate option with the sorted list
          # if found return True
          if nums[i:] + nums[:i] == numsSorted: 
              return True
        return False