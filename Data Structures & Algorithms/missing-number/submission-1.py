class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum=n*(n+1)//2
        ac_sum=sum(nums)
        return exp_sum-ac_sum

        