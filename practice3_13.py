def min(nums):
    return nums[0]
def max(nums):
    return nums[-1]
def mean(nums):
    return ((sum(nums) / len(nums)))
def mode(nums):
    mult = []
    for item in nums:
            a = nums.count(item)
            if a > 1:
                tup = [a, item]
                mult.append(tup)
    mult.sort()
    return (mult[0][1])

def main():
    nums = [8, 8, 3, 3, 3, 2, 3, 4, 5, 6, 7]
    sortedNums = sorted(nums)
    print(f'min: {min(sortedNums)}')
    print(f'max: {max(sortedNums)}')
    print(f'mean: {mean(sortedNums)}')
    print(f'mode: {mode(sortedNums)}')

main()

