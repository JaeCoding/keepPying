import pandas as pd


# 均方根误差
def RMSE(records):
    return sum([(rui - pui) * (rui - pui) for u, i, rui, pui in records.values]) \
           / float(len(records))


# 平均绝对误差
def MAE(records):
    return sum([abs(rui - pui) for u, i, rui, pui in records.values]) \
           / float(len(records))


data = {
    'u': [1, 2, 3, 4, 5],  # 用户id
    'i': [1, 2, 3, 4, 5],  # 电影id
    'rui': [5, 2, 5, 6, 1],  # 用户u对电影i的实际评分
    'pui': [7, 4, 9, 3, 8],  # 算法计算的用户u对电影i的 预测评分
}
df = pd.DataFrame(data, index=['1', '2', '3', '4', '5'], columns=['u', 'i', 'rui', 'pui'])
r = RMSE(df)
b = MAE(df)
print(r)
print(b)


