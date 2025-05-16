import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def get_deb_files(full_list, f, url, package_list, found, depth=0):
    """
    Recursively explores all subdirectories of the given URL and collects specific `.deb` files
    from the provided package list.
    
    Args:
    - url: URL of the directory to scrape.
    - package_list: List of specific package names you're interested in (without version info).
    - depth: Current recursion depth (used to avoid infinite loops).
    
    Returns:
    - A list of `.deb` file URLs that match the package list.
    """
    # Limit the recursion depth to avoid over-exploration
    if depth > 10:
        return []

    # Send GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page at {url}")
        return []

    # Parse the content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the links in the page
    links = soup.find_all('a')
    
    deb_files = []
    
    for link in links[4:]:
        href = link.get('href')
        full_url = urljoin(url, href)
        
        # If the link is a .deb file, check if it matches a package in the list
        if href.endswith('.deb'):
            full_list.write(f'{full_url}\n')
            for idx, package in enumerate(package_list):
                if package in href:  # Match package name (without version)
                    deb_files.append(full_url)
                    f.write(f'{full_url}\n')
                    found[idx] = 1
        
        # If it's a subdirectory, recursively explore it
        elif href.endswith('/'):
            deb_files.extend(get_deb_files(full_list, f, full_url, package_list, found, depth + 1))
    
    return deb_files

def load_package_list(file_path):
    """
    Loads a list of package names from a file (one per line).
    
    Args:
    - file_path: Path to the text file containing the package names.
    
    Returns:
    - A list of package names.
    """
    with open(file_path, 'r') as f:
        package_list = [line.strip() for line in f.readlines()]
    return package_list

if len(sys.argv) < 4:
    print("Usage: ubuntu_scraper.py <package_list_file> <output_file> <full_list_file>\n\n")
    print("package_list_file: Path to the file containing package names (one per line)")
    print("output_file: Path to the file where matching .deb URLs will be saved")
    print("full_list_file: Path to the file where all .deb URLs will be saved\n\n")
    print("Example: python ubuntu_scraper.py ../debian/package_list.txt ../debian/package_url.txt ../targetOS/package_url_port_ubuntu.txt")
    sys.exit(1)

package_list_file = sys.argv[1]
output_file = sys.argv[2]
full_list_file = sys.argv[3]

f = open(output_file, 'w')
full_list = open(full_list_file, 'w')

# Load the package names from the file
package_list = load_package_list(package_list_file)
found = [0] * len(package_list)

# URL to the pool/main directory
base_url = "http://ports.ubuntu.com/pool/"
deb_files = get_deb_files(full_list, f, base_url, package_list, found)

# Print out the list of .deb files found for the specified packages
if deb_files:
    print(f"Found {len(deb_files)} matching .deb files:")
    for deb in deb_files:
        print(deb)
else:
    print("No matching .deb files found.")

not_found = 0
for i in range(len(found)):
    print(package_list[i], found[i])
    if found[i] == 0:
        not_found = not_found + 1
        print(f'Did not find: {package_list[i]}\n')

print(f'Total packages not found: {not_found}')
print(f'Total packages: {len(package_list)}')
f.close()
full_list.close()