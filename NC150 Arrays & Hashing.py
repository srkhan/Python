from ast import List

class Solution:
    # Problem link: https://leetcode.com/problems/contains-duplicate/
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1st Approach with sorting the list and then comparing adjacent values
        # Time: O(nlogn) Space: O(1)
        '''
        if len(nums) == 1:
            return False
        nums.sort()
        for i, n in enumerate(nums):
            if nums[i] == nums[i-1]:
                return True
        return False
        '''
        # 2nd Approach with using a hashmap, iterate through list and add values if not in hashmap and return True and exit if n is already in hashmap
        # Time: O(n) Space: O(n) using extra memory for hashmap (worst case hashmap takes up as much space as list length -1 so n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False