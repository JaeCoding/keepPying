class Solution:
    def calculateCounterValues(self, arr):
        # 初始化结果数组，长度与输入数组相同，所有元素初始值为0
        result = [0 for _ in arr]
        # 初始化左边元素的总和为0
        left_sum = 0
        # 初始化左边元素的数量为0
        left_count = 0

        # 遍历输入数组
        for i in range(len(arr)):
            if i == 0:
                # 对于数组的第一个元素，左边没有元素，故计数器值为0
                result[i] = 0
            else:
                # 计算当前元素的计数器值
                result[i] = arr[i] * left_count - left_sum
            # 更新左边元素的总和和数量
            left_sum += arr[i]
            left_count += 1

        return result

    def test(self):
        # 测试用例
        test_cases = [
            ([2, 4, 3], [0, 2, 0]),  # 给定的示例
        ]

        # 遍历测试用例，验证结果
        for inputs, expected in test_cases:
            result = self.calculateCounterValues(inputs)
            assert result == expected, f"Test with input {inputs} failed with result {result}. Expected: {expected}"
        # 打印测试通过的消息
        print("All test cases passed.")


# 实例化Solution并运行测试方法
Solution().test()
