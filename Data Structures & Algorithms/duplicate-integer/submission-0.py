class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bank = set()

        for num in nums:
            if num in bank:
                return True
            else:
                bank.add(num)

        return False