import requests
import gzip
import sys
from io import BytesIO

# Change this to target a different Kubernetes version
K8S_VERSION = "v1.29"
BASE_URL = f"https://pkgs.k8s.io/core:/stable:/{K8S_VERSION}/deb/"


def parse_packages(arch, outfile):
    url = BASE_URL + "Packages.gz"
    print(f"Downloading {url}")

    r = requests.get(url, stream=True)

    if r.status_code != 200:
        print(f"Failed to download: {url}")
        return

    with gzip.open(BytesIO(r.content), "rt", encoding="utf-8", errors="ignore") as f:
        pkg_name = None
        filename = None
        pkg_arch = None

        for line in f:
            line = line.strip()

            if line.startswith("Package:"):
                pkg_name = line.split(":", 1)[1].strip()

            elif line.startswith("Filename:"):
                filename = line.split(":", 1)[1].strip()

            elif line.startswith("Architecture:"):
                pkg_arch = line.split(":", 1)[1].strip()

            elif line == "":
                # End of one package entry
                if filename and pkg_arch == arch:
                    full_url = BASE_URL + filename
                    outfile.write(full_url + "\n")
                    print(f"{pkg_name} -> {full_url}")

                pkg_name = None
                filename = None
                pkg_arch = None


def main(arch, output_file):
    with open(output_file, "w") as out:
        parse_packages(arch, out)


if len(sys.argv) < 3:
    print("Usage: kubernetes_packages.py <architecture> <output_file>")
    print("Example: python kubernetes_packages.py arm64 k8s_deb_urls.txt")
    sys.exit(1)

arch = sys.argv[1]
output_file = sys.argv[2]

main(arch, output_file)

print("Done.")