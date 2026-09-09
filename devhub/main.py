import shutil
import subprocess
import time
import os

tools = ["python", "git", "docker", "node", "gcc", "java", "steam"]

def check_tools(tools):
    results = {}

    for tool in tools:
        result = shutil.which(tool)
        results[tool] = result

    return results

results = check_tools(tools)
print(results)


def print_tools():

    for tool in results:
        if results[tool]:
            print(f"{tool} is installed")
        else:
            print(f"{tool} is not installed")

print_tools()


result = subprocess.run(
    [tools[0], "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)