def restricted(nums):
    # Add your solution here
    return restricted(nums[1:]) + nums[0] if nums else 0
