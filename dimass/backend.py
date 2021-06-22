import subprocess


def balaboba(context):
    query = context.get("query")
    style = context.get("style")
    try:
        process = subprocess.Popen(["./fetch.sh", f"{query}", f'{style}'], stdout=subprocess.PIPE)
        process.wait()
        output = process.stdout.read()
    except:
        return None
    return output.decode("utf-8")


if __name__ == '__main__':
    print(balaboba({"query": "d", "style": 1}))
