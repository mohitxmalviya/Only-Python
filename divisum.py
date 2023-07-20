def calculate_sum_distinction(m, n):
    # Calculate the sum of integers not divisible by m
    not_divisible_sum = sum(i for i in range(1, n+1) if i % m != 0)

    # Calculate the sum of integers divisible by m
    divisible_sum = sum(i for i in range(1, n+1) if i % m == 0)

    # Calculate the distinction between the two sums
    distinction = not_divisible_sum - divisible_sum

    return distinction

# Test the function
m = int(input())
n = int(input())
result = calculate_sum_distinction(m, n)
print(result)
