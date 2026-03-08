# getDebianPackageUrl
Scripts for getting urls given the deb package names

<h1>Usage</h1>

Pull debian packages and all dependencies on a debian machine to a directory and put the names to a text file
```
mkdir packages
cd packages
sudo ../source/get_packages.sh build-essential
cd ../source
python ./package_to_text.py ./packages package_list.txt
```

The current implementation gets packages for Ubuntu 22.04.
```
python ubuntu_packages.py 22.04 arm64 full_package_list_url.txt
python find_package.py package_list.txt package_url.txt full_package_list_url.txt
```

On your non Debian based machine get all the packages
```
mkdir packages
cd packages
./batch_wget.sh ../source/package_list.txt
```
