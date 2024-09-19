import os

ru_dir = os.getcwd()
counter = 0

for addr, _ , files in os.walk(ru_dir):
    for file in files:
        if file in files:
            if file.endswith(".md"):
               counter += 1

print(counter)
