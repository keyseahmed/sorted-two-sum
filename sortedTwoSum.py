def sortedTwoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            # Adjust indices to be 1-based
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    # Since the problem assumes exactly one solution, this line is optional
    # return [-1, -1]
    # Alternatively, you could raise an exception
    raise ValueError("No two sum solution exists")

# Example usage:
nums = [1, 2, 3, 4, 5]
print(sortedTwoSum(nums, 3))  # Output should be [1, 2]
