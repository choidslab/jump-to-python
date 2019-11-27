with open('test.txt', 'r') as f:
    lines = f.readlines()
    target = "java"

    for line in lines:
        if target in line:
            test = line.replace(target, 'python')
            with open('test.txt', 'a') as f:
                f.write(test)
        else:
            with open('test.txt', 'w') as f:
                f.write(line)
