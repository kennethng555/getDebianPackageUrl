# getDebianPackageUrl
Web scraper for getting urls given the deb package names

<h1>**Usage**</h1>
Pull debian packages and all dependencies on a debian machine to a directory and put the names to a text file
```
mkdir packages
cd packages
sudo ../get_packages.sh build-essential
cd ..
python ./package_to_text.py ./packages
```

The current implementation gets packages for Ubuntu 22.04. The full list of packages are in <em>full_package_list.txt.zip</em>
```
unzip full_package_list.txt.zip
python find_package.py
```

If needed to pull from another repository, modify the ubuntu_scraper.py and find_package.py does not need to be run.

On your non Debian based machine get all the packages
```
mkdir packages
cd packages
./batch_wget.sh ../package_list.txt
```