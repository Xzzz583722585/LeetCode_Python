class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i] = [num ^ 1 for num in A[i][::-1]]

        return A


if __name__ == "__main__":
    A = [[1, 1, 0],
         [1, 0, 1],
         [0, 1, 1]]
    print(Solution().flipAndInvertImage(A))
