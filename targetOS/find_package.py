import sys

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

if len(sys.argv) < 3:
    print("Usage: ubuntu_scraper.py <package_list_file> <output_file> <full_list_file>\n\n")
    print("package_list_file: Path to the file containing package names (one per line)")
    print("output_file: Path to the file where matching .deb URLs will be saved")
    print("full_list_file: Path to the file where all .deb URLs are saved\n\n")
    print("Example: python ubuntu_scraper.py ../debian/package_list.txt ../debian/package_url.txt ../targetOS/package_url_port_ubuntu.txt")
    sys.exit(1)

package_list_file = sys.argv[1]
output_file = sys.argv[2]
full_list_file = sys.argv[3]

f = open(output_file, 'w')

# Load the package names from the file
package_list = load_package_list(package_list_file)
url_list = load_package_list(full_list_file)
found = [0] * len(package_list)

not_found = 0
for idx, package in enumerate(package_list):
  for url in url_list:
    if package in url:
        f.write(f'{url}\n')
        found[idx] = 1
  if found[idx] == 0:
    print(f'Package not found: {package}')
    not_found = not_found + 1

print(f'Total packages not found:{not_found}')
print(f'Total packages: {len(package_list)}')
f.close()