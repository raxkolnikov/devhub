import shutil
import subprocess
import time
import os

tools = ["python", "git", "docker", "node", "gcc", "java"]

def check_tools(tools):
    results = {}

    for tool in tools:
        result = shutil.which(tool)
        results[tool] = result

    return results

results_dict = check_tools(tools)
print(results_dict)

def get_version(results_dict):
    for tool in results_dict:
        version = subprocess.run([tool, "--version"],
        capture_output = True,
        text = True
        )

        return version.stdout

print(get_version(results_dict))


def print_tools():

    for tool in results_dict:
        if results_dict[tool]:
            print(f"{tool} is installed")
        else:
            print(f"{tool} is not installed")

print_tools()


