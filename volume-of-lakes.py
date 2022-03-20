def trap(self, height):
    left_index, right_index = 0, len(height) - 1
    left_max, right_max = 0, 0
    output = 0
    while left_index < right_index:
        if height[left_index] <= height[right_index]:
            left_max = max(left_max, height[left_index])
            output += max(0, left_max - height[left_index])
            left_index += 1
        else:
            right_max = max(right_max, height[right_index])
            output += max(0, right_max - height[right_index])
            right_index -= 1
    return output