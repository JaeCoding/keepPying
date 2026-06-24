def minMaxDistanceAfterRemovingOnePoint(points):
    # 先計算最大的x+y, 最小的x+y, 最大的x-y, 最小的x-y
    max_plus, min_plus = float('-inf'), float('inf')
    max_minus, min_minus = float('-inf'), float('inf')
    for x, y in points:
        max_plus = max(max_plus, x + y)
        min_plus = min(min_plus, x + y)
        max_minus = max(max_minus, x - y)
        min_minus = min(min_minus, x - y)

    # 計算移除某一點後的最大距離
    result = float('inf')
    for x, y in points:
        # 移除當前點後，重新計算四個極值
        max_plus_new = max_plus if max_plus != x + y else max(x + y for x, y in points if x + y != max_plus)
        min_plus_new = min_plus if min_plus != x + y else min(x + y for x, y in points if x + y != min_plus)
        max_minus_new = max_minus if max_minus != x - y else max(x - y for x, y in points if x - y != max_minus)
        min_minus_new = min_minus if min_minus != x - y else min(x - y for x, y in points if x - y != min_minus)
        # 計算移除後的最大距離
        max_dist = max(max_plus_new - min_plus_new, max_minus_new - min_minus_new)
        result = min(result, max_dist)

    return result

# 示例測試
points1 = [[3,10],[5,15],[10,2],[4,4]]
points2 = [[1,1],[1,1],[1,1]]
print(minMaxDistanceAfterRemovingOnePoint(points1))  # 輸出應為 12
print(minMaxDistanceAfterRemovingOnePoint(points2))  # 輸出應為 0
