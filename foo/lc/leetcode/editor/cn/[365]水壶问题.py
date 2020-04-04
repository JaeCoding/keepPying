# You are given two jugs with capacities x and y litres. There is an infinite am
# ount of water supply available. You need to determine whether it is possible to 
# measure exactly z litres using these two jugs. 
# 
#  If z liters of water is measurable, you must have z liters of water contained
#  within one or both buckets by the end. 
# 
#  Operations allowed: 
# 
#  
#  Fill any of the jugs completely with water. 
#  Empty any of the jugs. 
#  Pour water from one jug into another till the other jug is completely full or
#  the first jug itself is empty. 
#  
# 
#  Example 1: (From the famous "Die Hard" example) 
# 
#  
# Input: x = 3, y = 5, z = 4
# Output: True
#  
# 
#  Example 2: 
# 
#  
# Input: x = 2, y = 6, z = 5
# Output: False
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 使用状态转移  加搜索。此方法会爆栈，修改为用栈替代递归
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        x_remain, y_remain = 0, 0
        seen = set()

        def recur(x_now, y_now) -> bool:
            if x_now == z or y_now == z or x_now + y_now == z:
                return True
            if (x_now, y_now) in seen:
                return False
            seen.add((x_now, y_now))
            # 加满A\加满B
            add_a = recur(x, y_now)
            add_b = recur(x_now, y)
            # 倒掉A\倒掉B
            drain_a = recur(0, y_now)
            drain_b = recur(x_now, 0)
            # a->b  b->a
            to_b_water = min(x_now, y - y_now)
            to_b = recur(x_now - to_b_water, y_now + to_b_water)
            to_a_water = min(x - x_now, y_now)
            to_a = recur(x_now + to_a_water, y_now - to_a_water)

            return add_a or add_b or drain_a or drain_b or to_b or to_a

        return recur(0, 0)

    def canMeasureWater2(self, x:int, y:int, z:int) -> bool:

        seen = set()
        # 用栈来保存上一位置的状态
        stack = [(0, 0)]
        while stack:
            # 弹出表示消费一个栈元素
            x_now, y_now = stack.pop()
            if x_now == z or y_now == z or x_now + y_now == z:
                return True
            if (x_now, y_now) in seen:
                continue
            seen.add((x_now, y_now))
            # 全部可能状态添加到栈中，类似bfs哦
            # 加满A\加满B
            stack.append((x, y_now))
            stack.append((x_now, y))
            # 倒掉A\倒掉B
            stack.append((0, y_now))
            stack.append((x_now, 0))
            # a->b  b->a
            to_b_water = min(x_now, y - y_now)
            stack.append((x_now - to_b_water, y_now + to_b_water))
            to_a_water = min(x - x_now, y_now)
            stack.append((x_now + to_a_water, y_now - to_a_water))
        return False

    def canMeasureWater3(self, x, y, z) -> bool:
        # 0 是没有最大公约数的
        def gcb(a: int, b: int) -> int:
            m = max(a, b)
            n = min(a, b)
            if m % n == 0:
                return n
            else:
                return gcb(n, m % n)
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        # 贝祖定理， ax+by=z成立的条件是，z是(x,y)最大公约数的倍数
        return z % gcb(x, y) == 0











a = Solution().canMeasureWater2(3, 4, 5)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
