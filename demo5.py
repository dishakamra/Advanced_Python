'''
OS Module
import os
p = os.path.join("lab", "nested", "notes.txt")
print(os.path.dirname(p)) #lab/nested
print(os.path.basename(p)) # notes.txt
print(os.path.splitext(p))
print(os.path.abspath(p))
'''

'''
Path, directories, file names

from pathlib import Path
p = Path("lab/nested/notes.txt")
print(p.parent, p.name, p.suffix, p.stem)
print(p.with_suffix(".md"))
'''

'''
Walking directory trees

import os
for root, dirs, files in os.walk("lab"):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        full = os.path.join(root, f)
        print("-->", full)

'''

# Env variables
import os

#Read
print(os.environ.get("HOME") or os.environ.get("USERPROFILE"))
print(os.environ.get("MY_APP_MODE","dev"))

# Expand in strings
print(os.path.expandvars("Path is: $PATH"))



