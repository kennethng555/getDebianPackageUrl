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

# Path to your package_list.txt file
package_list_file = "../debian/package_list.txt"
f = open('../debian/package_url.txt', 'w')
full_list_file = "./full_package_url.txt"

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