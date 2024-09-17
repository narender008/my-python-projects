import os

path = os.environ.get("PATH", "")
home = os.environ.get("HOME", "")

print(f"Env variable are \n\nPATH: {path}\n\nHOME: {home}")
