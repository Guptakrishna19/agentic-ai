class Solution(object):
    def removeElement(self, nums, val):
        c=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c]=nums[i]
                c+=1
        return c

nums=[12,34,2,2,12,2,0,1,2,2,4,5]
val=2
k=Solution().removeElement(nums,val)
print(k)
print(nums[:k])