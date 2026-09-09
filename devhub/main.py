import shutil

result = shutil.which("python")

if result:
    print("Python is installed")
else:
    print("Python is not installed")

result2 = shutil.which("git")

if result:
    print("Git is installed")
else:
    print("Git is not installed")