import shutil
import subprocess
import time
import os

# List of tools

tools = ["python", "git", "docker", "node", "gcc", "java"]

# Check if the tool is available in user's system

def check_tools(tools):
    results = {}

    for tool in tools:
        result = shutil.which(tool)
        results[tool] = result

    return results

results_dict = check_tools(tools)
print(results_dict)

# Get tool's version if it's installed through subprocess

def get_version(results_dict):
    results = {}

    for tool in results_dict:
        if results_dict[tool]:
            results[tool] = subprocess.run(
            [tool, "--version"],
            capture_output = True,
            text = True
            ).stdout

    return results

print(get_version(results_dict))

# Just a simple function to print tools

def print_tools():

    for tool in results_dict:
        if results_dict[tool]:
            print(f"{tool} installed")
        else:
            print(f"{tool} not installed")

print_tools()


