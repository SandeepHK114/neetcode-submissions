class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_val = set()
        for i in nums:
            if i not in unique_val:
                unique_val.add(i)
            else:
                return True
        else:
            return False