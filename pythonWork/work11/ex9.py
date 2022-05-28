nums = [1,2,3]
for j in range(1,len(nums)):
    nums[j] = nums[j] + nums[j-1]
print(nums)