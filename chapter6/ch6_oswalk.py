import os

DIRNAME = 'd:/'

for (path, dir, files) in os.walk(DIRNAME):
    print(files)