# Build records manually (id, temp*10, flag)
records = [
    (1, 235, 1),   # 23.5°C
    (2, -15, 0),   # -1.5°C
    (3, 402, 1),   # 40.2°C
]

# Write 4 bytes per record: [id][temp low byte][temp high byte][flag]
with open("records.bin", "wb") as f:
    for rec_id, temp10, flag in records:
        temp = temp10 & 0xFFFF  # keep 16 bits (two bytes)
        low = temp & 0xFF
        high = (temp >> 8) & 0xFF
        f.write(bytes([rec_id, low, high, flag]))

# Read them back knowing the layout
out = []
with open("records.bin", "rb") as f:
    blob = f.read()

for i in range(0, len(blob), 4):
    rec_id = blob[i]
    low = blob[i+1]
    high = blob[i+2]
    flag = blob[i+3]

    temp16 = (high << 8) | low     # reconstruct signed 16-bit
    if temp16 & 0x8000:            # if sign bit set
        temp16 -= 0x10000          # convert to negative

    out.append((rec_id, temp16 / 10, flag))

print(out)
# [(1, 23.5, 1), (2, -1.5, 0), (3, 40.2, 1)]
