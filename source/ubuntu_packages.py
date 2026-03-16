import requests
import gzip
import sys

# Ubuntu version -> codename mapping
UBUNTU_VERSIONS = {
    "24.04": "noble",
    "23.10": "mantic",
    "23.04": "lunar",
    "22.10": "kinetic",
    "22.04": "jammy",
    "20.04": "focal",
    "18.04": "bionic",
    "16.04": "xenial"
}

COMPONENTS = [
    "main",
    "universe",
    "multiverse",
    "restricted"
]


def get_base_url(arch):
    if arch in ["amd64", "i386"]:
        return "https://archive.ubuntu.com/ubuntu/"
    else:
        return "http://ports.ubuntu.com/"


def parse_packages(url, base_url, outfile):

    print(f"Downloading {url}")

    r = requests.get(url, stream=True)

    if r.status_code != 200:
        print(f"Failed: {url}")
        return

    with gzip.open(r.raw, "rt", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("Filename:"):
                path = line.split("Filename:")[1].strip()
                outfile.write(base_url + path + "\n")


def main(version, arch, output_file):

    if version not in UBUNTU_VERSIONS:
        print(f"Unsupported Ubuntu version: {version}")
        print("Supported versions:", ", ".join(UBUNTU_VERSIONS.keys()))
        sys.exit(1)

    base_url = get_base_url(arch)
    codename = UBUNTU_VERSIONS[version]

    releases = [
        codename,
        f"{codename}-updates",
        f"{codename}-security"
    ]

    with open(output_file, "w") as out:

        for rel in releases:
            for comp in COMPONENTS:

                url = f"{base_url}dists/{rel}/{comp}/binary-{arch}/Packages.gz"

                parse_packages(url, base_url, out)


if len(sys.argv) < 4:
    print("Usage: ubuntu_packages.py <ubuntu_version> <architecture> <output_file>")
    print("Example: python ubuntu_packages.py 22.04 arm64 deb_urls.txt")
    sys.exit(1)

version = sys.argv[1]
arch = sys.argv[2]
output_file = sys.argv[3]

main(version, arch, output_file)

print("Done.")