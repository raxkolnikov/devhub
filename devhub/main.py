import shutil

tools = ["python", "git", "docker", "node", "gcc", "java", "steam", "fserrfr"]

def check_tools():
    results = {}

    for tool in tools:
        result = shutil.which(tool)
        results[tool] = result

    return results

results = check_tools()
print(results)


def print_tools():

    for tool in results:
        if results[tool]:
            print(f"{tool} is installed")
        else:
            print(f"{tool} is not installed")

print_tools()