nums = [1,2,3,4,5,6,7]
target = 6

def binarySearch(nums: [int], target: int):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
print(binarySearch(nums,target))