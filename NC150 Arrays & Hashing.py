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
        # TODO review this again
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

    # Problem link: https://leetcode.com/problems/valid-palindrome/        
    def isPalindrome(self, s: str) -> bool:
        # 1st approach, create new str, filter out non alphanumeric characters, add alphanumeric lowercase chars to str and check if its equal
        # to reverse of the string, uses extra memory for new str and reverse of it and built in python functions like isalnum and isdigit
        # Time: O(n) Space: O(n)
        newStr = ""

        for c in s:
            if c.isalnum() or c.isdigit():
                newStr += c.lower()
        return (newStr == newStr[::-1])
    
        # 2nd approach, using pointers check if L (leftmost alphanumeric char in str s) and R (rightmost alphanumeric char in str s) are equal. If not return (NOT a palindrome)
        # if so increment L and decrement R until they meet in the middle char (str is odd) or L and R passes each other and return (IS a palindrome). 
        # To determine if a char is alphanumeric we can use ascii values and skip non alphanumeric chars in string s
        # Time: O(n) Space: O(1) no extra space needed for this soln
        L, R = 0, len(s) -1

        while L < R:
            #these loops are done to skip over nonalphanuemric chars
            while L < R and not self.alphaNum(s[L]):
                L += 1
            while R > L and not self.alphaNum(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L = L + 1
            R = R - 1
        return True

        # func will return true or false if it is alphanumeric or not
        def alphaNum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))     
        
    # Probelm link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    def maxProfit(self, prices: List[int]) -> int:
        # Approach: sliding window problem, first set lowest price to be 1st elem in arr and initalize profit to be zero, 
        # then check if arr[i] is less than lowest price, if so make lowest price = arr[i]. Then take the maximum of profit and arr[i] - lowest price and set it to profit
        # After finishing iteration of arr maximum profit will be in profit var
        # Time: O(n) Space: O(1), no space used just iterating thru prices list once to find max profit
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        return profit
        # soln 2 slightly different, have left(buy) and right(sell) pointer, initialize r to be next element after l, loop through prices and check if left(buy) is 
        # less than right(sell) if so find profit (arr[r] - arr[l]) and then check the maximum between max profit and profit and set highest # to max P
        # if left pointer (buy) is not less than right pointer (sell), make right pointer(sell) the new left pointer(buy), and afterwards iterate thru while loop
        # After finishing iteration of prices array maximum profit will be in maxP var
        # Time: O(n) Space: O(1), no space used just iterating thru prices list once to find max profit
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+= 1
        return maxP