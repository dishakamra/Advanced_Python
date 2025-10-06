import os
from pathlib import Path

#current working directory
print(os.getcwd())

# Make directories
os.makedirs("lab/nested", exist_ok=True)

# List entries
print(os.listdir("lab"))
with os.scandir("lab") as it:
    for entry in it:
        print(entry.name, "dir?", entry.is_dir(), "file?", entry.is_file())

Path("lab/hello.txt").write_text("hi again") # create a file
os.replace("lab/hello.txt","lab/greeting.txt")

st=os.stat("lab/greeting.txt") # File metadata
print(st.st_size, "bytes")