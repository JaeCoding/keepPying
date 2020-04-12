# English description is not available for the problem. Please switch to Chinese
# .


# leetcode submit region begin(Prohibit modification and deletion)
import queue


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def get_bit_sum(num: int):
            sum = 0
            while num > 0:
                sum += num % 10
                num = int(num / 10)
            return sum

        count = 0
        visited = set()
        visited.add((0, 0))
        now = queue.Queue()
        now.put((0, 0))
        # 注意 不能while queue
        while not now.empty():
            (i, j) = now.get()
            print((i,j))
            count += 1
            # 上
            if j - 1 >= 0 and (i, j-1) not in visited and get_bit_sum(i) + get_bit_sum(j - 1) <= k:
                now.put((i, j-1))
                visited.add((i, j-1))
            if j + 1 < n and (i, j+1) not in visited and get_bit_sum(i) + get_bit_sum(j + 1) <= k:
                now.put((i, j+1))
                visited.add((i, j + 1))
            if i - 1 >= 0 and (i-1, j) not in visited and get_bit_sum(i-1) + get_bit_sum(j) <= k:
                now.put((i-1, j))
                visited.add((i-1, j))
            if i + 1 < m and (i+1, j) not in visited and get_bit_sum(i+1) + get_bit_sum(j) <= k:
                now.put((i+1, j))
                visited.add((i+1, j))
        return count

# a = Solution().movingCount(2,3,1)
# a = Solution().movingCount(3,1,0)
a = Solution().movingCount(3,2,17)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
