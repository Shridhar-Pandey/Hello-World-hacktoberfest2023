class Solution:
    def getPermutation(self, n, k):
        factorials = [1]
        for i in range(1, n):
            factorials.append(i * factorials[-1])
        k -= 1
        permutation = []
        nums = [i + 1 for i in range(n)]
        for i in range(n - 1, -1, -1):
            index = k // factorials[i]
            k %= factorials[i]
            permutation.append(nums[index])
            nums.pop(index)
        return ''.join(str(num) for num in permutation)

# Input
n = int(input("Enter n: "))
k = int(input("Enter k: "))

# Output
solution = Solution()
result = solution.getPermutation(n, k)
print(result)
