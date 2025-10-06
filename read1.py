#Reading/Writing with context manager
from pathlib import Path
p = Path("example.txt")

#write text
p.write_text("hello\n")

# append
with p.open("a", encoding="utf-8") as f:
    print("world", file=f)

# read
text = p.read_text(encoding="utf-8")
print(text)