# Write raw bytes
with open("demo.bin", "wb") as f:      # 'wb' = write binary
    f.write(b"\x01\x02\x03\x04")       # four raw bytes

# Read them back
with open("demo.bin", "rb") as f:      # 'rb' = read binary
    data = f.read()
    print(data)                         # b'\x01\x02\x03\x04'
    print(list(data))                   # [1, 2, 3, 4]
