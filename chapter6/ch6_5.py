import sys

if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]

    with open(src, 'r') as f:
        tab_content = f.read()

    space_content = tab_content.replace('\t', " "*4)

    with open(dst, 'w') as f:
        f.write(space_content)
