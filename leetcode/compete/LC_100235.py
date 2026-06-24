def max_bottles(numBottles, numExchange):
    # 已喝的水瓶数量初始化为最初的满水瓶数
    total_drunk = 0
    # 当前空瓶数量初始化为0
    empty_bottles = 0
    full_bottles = numBottles

    # 当满水瓶数量大于0时，进行循环
    while full_bottles > 0:
        # 喝掉所有满水瓶，满水瓶数量变为0，空瓶数量增加
        total_drunk += full_bottles
        empty_bottles += full_bottles
        full_bottles = 0

        # 使用空水瓶交换满水瓶

        # 更新空瓶数量
        if empty_bottles >= numExchange:
            empty_bottles -= numExchange
            full_bottles += 1
            numExchange += 1

    # 返回总共喝掉的水瓶数量
    return total_drunk

# 测试代码
example1 = max_bottles(13, 6)  # 应当输出15
print(example1)
example2 = max_bottles(10, 3)  # 应当输出13
print(example2)
