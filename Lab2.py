'''
Normalize & list large Python files
-----------------------------------
Task: Given a start directory, list all *.py files whose size is ≥ N KB, printing a normalized absolute path and size. 
Ignore hidden directories.
'''
import os

def large_py_files(root: str, min_kb: int = 10):
    min_bytes = min_kb * 1024
    for r, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if name.endswith(".py"):
                full = os.path.abspath(os.path.join(r, name))
                try:
                    if os.path.getsize(full) >= min_bytes:
                        print(f"{full}  ({os.path.getsize(full)} bytes)")
                except FileNotFoundError:
                    # File could disappear mid-walk; skip safely
                    pass

# Test
large_py_files(".", 5)

'''
Safe directory creation & writing

Task: Create build/assets/logs if missing. Write a README.md into build with a single line.
'''
import os
from pathlib import Path

root = Path("build")
(os.makedirs(root / "assets" / "logs", exist_ok=True))
readme = root / "README.md"
readme.write_text("# Build artifacts\n")
print("Created:", readme.resolve())

'''
Find duplicate filenames (case-insensitive)

Task: Walk a tree and report files that share the same name (ignoring case and extension). 
Example: Report.TXT and report.csv are duplicates by stem.
'''
import os
from collections import defaultdict
from pathlib import Path

def dup_stems(root: str):
    buckets = defaultdict(list)
    for r, _, files in os.walk(root):
        for f in files:
            stem = Path(f).stem.lower()
            buckets[stem].append(os.path.join(r, f))
    for stem, paths in buckets.items():
        if len(paths) > 1:
            print(f"[{stem}]")
            for p in paths:
                print("  -", p)

dup_stems("demo")

'''
Directory size by extension

Task: Produce a report of total bytes grouped by file extension under a directory (no hidden dirs). Sort by size desc.
'''
import os
from collections import Counter
from pathlib import Path

def size_by_ext(root: str):
    sizes = Counter()
    for r, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            full = os.path.join(r, f)
            try:
                ext = Path(f).suffix.lower() or "<noext>"
                sizes[ext] += os.path.getsize(full)
            except FileNotFoundError:
                pass
    for ext, total in sizes.most_common():
        print(f"{ext:8s} {total:>12,} bytes")

size_by_ext(".")

