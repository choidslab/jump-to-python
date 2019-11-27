with open('abc.txt', 'r') as f:
    data = f.readlines()
    reverse_data = reversed(data)

for item in reverse_data:
    with open('abc2.txt', 'a') as f:
        f.write(item)