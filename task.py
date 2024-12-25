#function that find the sum of numbers in a list
def listSum(nums:list[int]):
    totalSum=0
    for i in range(len(nums)):
        totalSum+=nums[i]
    return totalSum
