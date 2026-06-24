def maxFrequency(nums, freq):
    id_freq = {}  # Dictionary to keep track of the frequency of each ID.
    ans = []  # List to store the maximum frequency after each operation.

    max_freq = 0  # Keep track of the maximum frequency seen so far.
    for i in range(len(nums)):
        # Update the frequency of the current ID.
        if nums[i] in id_freq:
            id_freq[nums[i]] += freq[i]
            # If frequency drops to zero or below, remove the ID.
            if id_freq[nums[i]] <= 0:
                del id_freq[nums[i]]
        else:
            if freq[i] > 0:
                id_freq[nums[i]] = freq[i]

        # Only if we added frequency, check if it's a new max.
        if freq[i] > 0:
            max_freq = max(max_freq, id_freq[nums[i]])

        # After each operation, find the current max frequency if the dictionary is not empty.
        if id_freq:
            # This step ensures the max_freq is accurate in case the previous max was decreased or removed.
            current_max = max(id_freq.values())
            ans.append(current_max)
            max_freq = current_max  # Update max_freq with the current max value.
        else:
            ans.append(0)
            max_freq = 0  # Reset max_freq since the collection is empty.

    return ans


# Example usage:
nums = [2, 3, 2, 1]
freq = [3, 2, -3, 1]
print(maxFrequency(nums, freq))

nums = [5, 5, 3]
freq = [2, -2, 1]
print(maxFrequency(nums, freq))
