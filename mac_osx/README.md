# Gerrit Installer For Mac OSX

* This installation does the following, it creates a user called gerrit2, it installs in /var/lib/gerrit2.

* You can find already built pkg packages at https://github.com/paladox/gerrit-mac-installer/releases

* To build it your self do the following first

** chmod a+x installer.sh

** chmod a+x uninstaller/uninstaller.sh

** chmod a+x scripts/*

** chmod a+x uninstaller/scripts/*

** ./installer.sh

To create the uninstaller run the following script from bash (Note: You may need to do sudo ./uninstaller.sh)

cd uninstaller

** ./uninstaller.sh


Note: Some of these files came from https://phabricator.wikimedia.org/diffusion/ODDX/
