nums = [8, 8, 3, 3, 3, 2, 3, 4, 5, 6, 7]

def removeMult(nums):
    for item in nums:
        if nums.count(item) > 1:
            nums.remove(item)
    return nums

    
print(removeMult(nums))