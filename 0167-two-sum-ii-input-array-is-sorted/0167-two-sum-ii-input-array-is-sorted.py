class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l<=r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                while numbers[l] + numbers[r] < target:
                    l += 1
            else:
                r -= 1
        