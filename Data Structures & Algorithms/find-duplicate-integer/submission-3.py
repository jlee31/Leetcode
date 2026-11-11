class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # find the starting point
        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # reset slow
        slow = nums[0]

        # move them at the same timee
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow