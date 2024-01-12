class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initializes two pointers at first and last index of the array.
        low = 0
        high = len(nums) - 1

        # Runs until the two pointers are the same
        while low <= high:
            # Calculates the midpoint of the two pointers
            mid = (low + high) // 2
            # If midpoint is target, return mid index
            if nums[mid] == target:
                return mid
            # Adjusts pointers based on whether target is less than or greater than midpoint
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # If while loop completes without returning mid index, value is not in array
        return -1
