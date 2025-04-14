import os
import sys

f = open('./package_list.txt', 'w')

for file in os.listdir(sys.argv[1]):
    f.write(f'{file}')
    f.write('\n')

f.close()