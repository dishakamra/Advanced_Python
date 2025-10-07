import subprocess

# Simple: run and check exit code
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print("RC:", result.returncode)
print("OUT:", result.stdout.strip())
print("ERR:", result.stderr.strip())

# With custom environment and timeout
import os
env = os.environ.copy()
env["MY_FLAG"] = "1"
try:
    out = subprocess.run(
        ["python", "-c", "import os; print(os.environ.get('MY_FLAG'))"],
        capture_output=True, text=True, env=env, timeout=5
    )
    print("Child saw:", out.stdout.strip())
except subprocess.TimeoutExpired:
    print("Process timed out.")

# Streaming long-running process (no capture)
proc = subprocess.Popen(["python", "-c", "print('hello'); import time; time.sleep(1); print('bye')"])
proc.wait()
print("Exited with", proc.returncode)
