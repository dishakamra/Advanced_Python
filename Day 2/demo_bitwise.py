a = 0b0101  # 5
b = 0b0011  # 3

print(bin(a & b))  # 0b0001 (1)
print(bin(a | b))  # 0b0111 (7)
print(bin(a ^ b))  # 0b0110 (6)
print(bin(a << 1)) # 0b1010 (10)
print(bin(a >> 1)) # 0b0010 (2)
