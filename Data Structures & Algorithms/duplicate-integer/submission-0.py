class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm=dict()
        for i in nums:
            if i in hm:
                return True
            hm[i]=i
        return False