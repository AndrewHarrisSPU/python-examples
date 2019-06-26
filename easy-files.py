import json


# Output formatting
# File IO

file = open("some-data.json")
data = file.read()
print(data)
file.close()

file = open("some-data.json")
ln = 1
while True:
    line = file.readline()
    if line:
        print(f"Line {ln}: {line}")
        ln += 1
    else:
        break
file.close()

file = open("more-data.txt", "w")
for i in range(1, 10):
    file.write(f"Number {i}\n")
file.close()

# JSON files
file=open("some-data.json")
data = json.load(file)
print(data)
print()
for o in data:
    for field in o:
        print(f"{field} = {o[field]} \n")
    print()



