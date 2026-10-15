class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        more=set()
        for num in nums:
            if num in more:
             return True
            more.add(num)
        return False