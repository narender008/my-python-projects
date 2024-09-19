import subprocess
import os

date = subprocess.run(["date"])

print(date.returncode)

result = subprocess.run(["host", "8.8"], capture_output=True)

print(result.returncode)
print(result.stderr)
print(os.environ.get("PATH"))

env = os.environ.copy()
# print(env["SHELL"])
env["PATH"] = os.pathsep.join(["new/path/in/path", env["PATH"]])
print(env["PATH"])
