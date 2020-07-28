import os

for file in os.listdir("."):
    if file.endswith(".html"):
        with open(file, "r+") as fp:
            content = fp.read().replace("file:///d:\\Projects\\data-diagrams\\proposal\\", "")
            fp.write(content)