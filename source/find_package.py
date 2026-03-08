import sys

def extract_package_name(url):
    """
    Extract package name from a .deb URL.
    Example:
    http://.../libssl1.1_1.1.1f-1ubuntu2_amd64.deb
    -> libssl1.1_1.1.1f-1ubuntu2_amd64.deb
    """
    return url.split('/')[-1]

def load_urls(file_path):
    urls = {}
    with open(file_path, 'r') as f:
        for line in f.readlines():
            url = line.strip()
            package_name = extract_package_name(url)
            urls[package_name] = url
    return urls

def load_package_list(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

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
url_list = load_urls(full_list_file)
found = [0] * len(package_list)

not_found = 0
for idx, package in enumerate(package_list):
    if package in url_list:
        f.write(f'{url_list[package]}\n')
        print(f'Found package: {package} -> {url_list[package]}')
        found[idx] = 1
    else:
        print(f'Package not found: {package}')
        not_found += 1

print(f'Total packages not found:{not_found}')
print(f'Total packages: {len(package_list)}')
f.close()