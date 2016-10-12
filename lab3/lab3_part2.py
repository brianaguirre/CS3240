__author__ = 'BrianAguirre'

import os
from os import path

my_path = os.getcwd()
files = [f for f in os.listdir(my_path) if path.isfile(f)]

file_names = []
for i in files:
    file_names.append(i)

num_lines = {}
for i in range(0, len(file_names)):
    with open(file_names[i]) as f:
        content = f.readlines()

    num_lines[i] = len(content)

for j in range (0, len(file_names)):
    print ("File name: " + file_names[j] + "    " + "Number of lines: "+ str(num_lines[j]))


if __name__ == "__main__":
    pass