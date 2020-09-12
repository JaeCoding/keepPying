# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。 
# 
#  
# 
#  示例: 
# 
#  输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"] 
#  Related Topics 字符串 回溯算法 
#  👍 378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []
        dot = []
        def dfs(index: int, count: int):
            # 已记录的点位，最多三个 .
            count += 1
            if count == 4:
                if int(s[index:]) <= 255:
                    if s[dot[2]:][0] == '0' and len(s[dot[2]:]) > 1:
                        return
                    a = s[0:dot[0]] + '.' + s[dot[0]: dot[1]] + '.' + s[dot[1]: dot[2]]+ '.' + s[dot[2]:]
                    result.append(a)
                return

            # 从index开始循环,
            for i in range(index + 1, len(s)):
                # 如果 s[index, i] <= 255 则在此处打点
                now = s[index:i]
                if now[0] == '0' and len(now) > 1:
                    continue
                if int(now) <= 255:
                    dot.append(i)
                    dfs(i, count)
                    dot.pop()

            count -= 1

        dfs(0, 0)
        return result

# a = Solution().restoreIpAddresses("2552551113")
a = Solution().restoreIpAddresses("010010")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
