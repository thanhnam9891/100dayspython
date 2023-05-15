def reverse(value):
    if value ==1:
        return 1
    else:
        result = value * reverse(value - 1)
        return result
print(reverse(2))