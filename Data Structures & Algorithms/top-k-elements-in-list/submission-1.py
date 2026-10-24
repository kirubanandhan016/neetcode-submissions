class Solution:
    def topKFrequent(self, nums, k):
        fre = {}

        for num in nums:
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1

        sorted_nums = sorted(fre, key=fre.get, reverse=True)
        return sorted_nums[:k]