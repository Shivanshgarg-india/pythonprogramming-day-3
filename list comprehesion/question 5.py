# Is y divisible by 2 or not?
# Is y divisible by 5 or not?
# If y satisfies both conditions, y is appended to num_list.

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
