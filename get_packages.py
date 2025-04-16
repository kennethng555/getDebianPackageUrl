import os
import sys

def clean_percent_line(line):
    percent_index = line.find('%')
    if percent_index == -1:
        return line  # No % found, return original line
    
    # Calculate start and end indexes to remove
    start = max(percent_index - 1, 0)
    end = percent_index + 3  # +1 for %, +2 for next two chars
    return line[:start] + line[end:]

f = open('./package_list.txt', 'w')

for file in os.listdir(sys.argv[1]):
    cleaned_file = clean_percent_line(file)
    f.write(f'{cleaned_file}')
    f.write('\n')

f.close()