def power_of_two(n):
    bit_count = 0
    while n != 0:
        bit_count += (n & 1)
        n = n >> 1
    return bit_count == 1

number = int(input("Enter a number: "))
power = 0
if power_of_two(number) is True:
    print(f"{number} is a power of two")
    while number != 1:
        number /= 2
        power += 1
    print(f"The power is {power}")
        
else:
    print(f"{number} is not a power of two")
