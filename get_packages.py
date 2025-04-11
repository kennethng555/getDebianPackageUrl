import os
from bs4 import BeautifulSoup

f = open('./package_list.txt', 'w')

for file in os.listdir('./packages'):
    f.write(f'{file}')
    f.write('\n')

f.close()