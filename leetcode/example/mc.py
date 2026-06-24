def find_longest_vowel_subsequence(s):
    vowels = "aeiou"
    n = len(s)
    start = 0  # 子字符串的起始位置
    max_len = 0  # 最长子字符串的长度
    max_substring = ""  # 最长的元音子字符串

    while start < n:
        subsequence = ""
        sequence_pos = 0  # 当前需要匹配的元音字母在vowels中的位置
        for i in range(start, n):
            if sequence_pos < len(vowels) and s[i] == vowels[sequence_pos]:
                subsequence += s[i]
                if sequence_pos < len(vowels) - 1:  # 如果不是'u'，则移动到下一个元音字母
                    sequence_pos += 1
            elif sequence_pos > 0 and s[i] == vowels[sequence_pos - 1]:
                # 允许重复的元音字母
                subsequence += s[i]
            # 如果找到了一个完整的元音序列
            if sequence_pos == len(vowels) - 1 and subsequence[-1] == 'u':
                if len(subsequence) > max_len:
                    max_len = len(subsequence)
                    max_substring = subsequence
        start += 1

    return max_substring


# 运行示例检验
example_inputs = ["iaaaeiouu", "aeeiou", "aeiou79aaeeioooouuu", "aieou", ""]
example_outputs = [find_longest_vowel_subsequence(input_str) for input_str in example_inputs]

print(example_outputs)
