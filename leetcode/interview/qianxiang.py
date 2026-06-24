# 给出两个只包含小写字母的字符串S和T。你可以做若干次以下操作：将S中的某个小写字母全部替换成另一个小写字母。请问是否能将S转换为T，如果能，应该如何操作。要求操作次数尽可能少。

# S = danny
# T = jessy
# [d:j, a:e, n:s]


# 可以引⼊的库和版本相关请参考 “环境说明”
# Please refer to the "Environmental Notes" for the libraries and versions that can be introduced.

def main():
    print('Talk is cheap. Show me the code.')


if __name__ == "__main__":
    main()


def isValidate(S, T):
    # Edge case check
    if len(S) != len(T):
        return []

    char_map = {}
    for s_char, t_char in zip(S, T):
        if s_char in char_map:  # if we find the map in previous char_map
            if char_map[s_char] != t_char:
                return []
        else:
            # check the map, it's invalid if it has multiple mapping for a char
            # if t_char in char_map.values():
            # char_map[s_char] = t_char
            # Add the mapping to map
            char_map[s_char] = t_char

    return [f"{k}:{v}" for k, v in char_map.items() if k != v]


S = "danny"
T = "jessy"

output = isValidate(S, T)
print(output)

S = "dannyyy"
T = "jessy"
output2 = isValidate(S, T)
print(output2)

S = "daany"
T = "jessy"
output3 = isValidate(S, T)
print(output3)

S = "danxy"
T = "jeesy"
output3 = isValidate(S, T)
print(output3)

S = ""
T = ""
output4 = isValidate(S, T)
print(output4)








