import sys

def sort_urls_by_architecture(input_file, repo_type):
    with open(input_file, 'r') as f:
        urls = f.readlines()

    arm64_urls = []
    armhf_urls = []
    amd64_urls = []
    i386_urls = []
    riscv64_urls = []
    powerpc_urls = []
    ppc64el_urls = []
    s390x_urls = []

    if repo_type == 'archive':
      for url in urls:
        url = url.strip()
        if url.endswith('amd64.deb'):
          amd64_urls.append(url)
        if url.endswith('i386.deb'):
          i386_urls.append(url)
        if url.endswith('all.deb'):
          amd64_urls.append(url)
          i386_urls.append(url)

      with open('data/package_url_amd64.txt', 'w') as f_amd:
        for url in amd64_urls:
          f_amd.write(url + '\n')
      with open('data/package_url_i386.txt', 'w') as f_i386:
        for url in i386_urls:
          f_i386.write(url + '\n')

    elif repo_type == 'port':
      for url in urls:
          url = url.strip()
          if url.endswith('arm64.deb'):
            arm64_urls.append(url)
          if url.endswith('armhf.deb'):
            armhf_urls.append(url)
          if url.endswith('riscv64.deb'):
            riscv64_urls.append(url)
          if url.endswith('powerpc.deb'):
            powerpc_urls.append(url)
          if url.endswith('ppc64el.deb'):
            ppc64el_urls.append(url)
          if url.endswith('s390x.deb'):
            s390x_urls.append(url)
          if url.endswith('all.deb'):
            arm64_urls.append(url)
            armhf_urls.append(url)
            riscv64_urls.append(url)

      with open('data/package_url_arm64.txt', 'w') as f_arm:
        for url in arm64_urls:
          f_arm.write(url + '\n')

      with open('data/package_url_armhf.txt', 'w') as f_armhf:
        for url in armhf_urls:
          f_armhf.write(url + '\n')

      with open('data/package_url_riscv64.txt', 'w') as f_riscv64:
        for url in riscv64_urls:
          f_riscv64.write(url + '\n')

      with open('data/package_url_powerpc.txt', 'w') as f_powerpc:
        for url in powerpc_urls:
          f_powerpc.write(url + '\n')

      with open('data/package_url_ppc64el.txt', 'w') as f_ppc64el:
        for url in ppc64el_urls:
          f_ppc64el.write(url + '\n')

      with open('data/package_url_s390x.txt', 'w') as f_s390x:
        for url in s390x_urls:
          f_s390x.write(url + '\n')


if len(sys.argv) < 3:
    print("Usage: split.py <package_url_file> <type>\n\n")
    print("file: Path to the file containing .deb URLs (one per line)")
    print("type: port or archive\n\n")
    print("Example: python split.py package_url_port_ubuntu.txt port")
    sys.exit(1)

file = sys.argv[1]
repo_type = sys.argv[2]
sort_urls_by_architecture(file, repo_type)
