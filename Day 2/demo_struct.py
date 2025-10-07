import struct

# Format: <B h B  means:
# <   little-endian
# B   unsigned byte     (id)
# h   signed short      (temperature * 10)
# B   unsigned byte     (flag)
fmt = "<BhB"

data = [
    (1, 235, 1),   # 23.5°C
    (2, -15, 0),   # -1.5°C
    (3, 402, 1),   # 40.2°C
]

# Pack and write
with open("rec_struct.bin", "wb") as f:
    for rec in data:
        f.write(struct.pack(fmt, rec[0], rec[1], rec[2]))

# Read and unpack
out = []
rec_size = struct.calcsize(fmt)
with open("rec_struct.bin", "rb") as f:
    blob = f.read()

for i in range(0, len(blob), rec_size):
    rec_id, temp10, flag = struct.unpack(fmt, blob[i:i+rec_size])
    out.append((rec_id, temp10 / 10, flag))

print(out)
# [(1, 23.5, 1), (2, -1.5, 0), (3, 40.2, 1)]
