class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n=set()
        for i in nums:
            if i in set_n:
                return True
            set_n.add(i)
        return False