def power_of_two(n):
    bit_count = 0
    while n != 0:
        bit_count += (n & 1)
        n = n >> 1
    return bit_count == 1
print(power_of_two(16))
