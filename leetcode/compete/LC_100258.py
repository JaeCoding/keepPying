from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:

        id_freq = {}  # 存储ID及其对应的频率
        ans = []  # 存储每一步操作后频率最高的ID数目
        for i in range(len(nums)):
            id_freq[nums[i]] = id_freq.get(nums[i], 0) + freq[i]  # 更新ID的频率
            if id_freq[nums[i]] <= 0:
                del id_freq[nums[i]]  # 如果某ID的频率为0或小于0，则从字典中删除

            if id_freq:  # 如果字典非空
                max_freq = max(id_freq.values())  # 找到当前最高频率
                # 正确计算最高频率的ID的总数目
                ans.append(max_freq)
            else:
                ans.append(0)  # 如果字典为空，说明集合为空，频率最高数目为0
        return ans


print(Solution().mostFrequentIDs([2, 8], [2, 2]))

