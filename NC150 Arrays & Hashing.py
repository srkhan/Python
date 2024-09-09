from ast import List

class Solution:
    # Problem link: https://leetcode.com/problems/contains-duplicate/
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1st Approach with sorting the list and then comparing adjacent values
        # Time: O(nlogn) Space: O(1)
        if len(nums) == 1:
            return False
        nums.sort()
        for i, n in enumerate(nums):
            if nums[i] == nums[i-1]:
                return True
        return False
        
        # 2nd Approach with using a hashmap, iterate through list and add values if not in hashmap and return True and exit if n is already in hashmap
        # Time: O(n) Space: O(n) using extra memory for hashmap (worst case hashmap takes up as much space as list length -1 so n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    # Problem link: https://leetcode.com/problems/valid-anagram/
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st approach, check if strings are same length, use hashamap to keep track of # of occurances of every character 
        # in each string, then go thru keys and check counts are the same
        # Time: O(s+t) or O(n) Space: O(s+t) or O(n)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
        # 2nd approach, using built in python counter
        # Time: O(n) Space: O(n)
        return Counter(s) == Counter(t)
    
        # 3rd approach
        # Time: O(1) Space: O(1), possibly more depending on how much space sorting takes up in pyton
        return sorted(s) == sorted(t)
    # Problem link: https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1st approach, use hashmap, iterate through nums check if diff (target - nums[i]) exists in hashmap, return index of diff and current index as pair
        # if diff doesnt exist add index of nums[i] to hashmap as key
        # Time: O(n) Space: O(n)
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums [i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i
