class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        total_zero = 0
        for n in nums:
            if n == 0:
                total_zero += 1
            else:
                product = product * n
        output = [0] * len(nums)
        for i in range(len(nums)):
            if total_zero > 1:
                output[i] = 0
            elif total_zero == 1:
                if nums[i] == 0:
                    output[i] = product
                else:
                    output[i] = 0
            else:
                output[i] = int((product/nums[i]))
        return output
            

        