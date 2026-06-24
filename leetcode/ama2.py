def find_first_discontinuous(nums, start, end):
    """
    Find the first discontinuous position in nums within the range [start, end].
    """
    if start > end:
        return None
    left, right = start, end
    while left < right:
        mid = (left + right) // 2
        # Check if the element is not at its expected position
        if nums[mid] != nums[start] + (mid - start):
            right = mid
        else:
            left = mid + 1
    # Check if the discovered index is actually discontinuous
    if left < len(nums) and nums[left] != nums[start] + (left - start):
        return left
    return None

def compress_using_binary_search(nums):
    result = []
    start = 0
    while start < len(nums):
        # Find the first discontinuous position
        discontinuous_index = find_first_discontinuous(nums, start, len(nums) - 1)
        if discontinuous_index is None:
            # If there's no discontinuity, add the remaining continuous segment
            result.append([nums[start], nums[-1]])
            break
        else:
            # Add the continuous segment till the discontinuous index
            result.append([nums[start], nums[discontinuous_index - 1]])
            start = discontinuous_index
    return result

# Example
input_nums = [1, 2, 3, 4, 7, 8, 10]
output = compress_using_binary_search(input_nums)
print(output)
