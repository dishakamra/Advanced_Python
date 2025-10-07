# Text - Bytes
text = "Hello, π!"
data = text.encode('utf-8') # Text --> bytes
print(data)
print(list(data))

roundtrip = data.decode('utf-8') # bytes --> Text
print(roundtrip)
