Gerrit Native Installation Packages
===================================
This project contains the native Gerrit installation packages for the most
popular platforms:

- Linux (RPM and Debian packages)
- MacOSX (DMG)
- Windows (MSI)

Linux RPM
---------
rpmbuild subdirectory contains the RPM source files to create a basic Gerrit
installation with the following options:

- site: /var/gerrit
- user: gerrit
- auth: development`_`become`_`any`_`account

### How to build

You need to have a Linux RPM machine with the rpmbuild utility installed.
Then execute the following steps from the cloned gerrit-installer project workspace:

1. ln -s rpmbuild ~/rpmbuild
2. rpmbuild -bb ~/rpmbuild/SPECS/gerrit.spec

RPM gets created under ~/rpmbuild/RPMS/noarch/gerrit-2.11-1.noarch.rpm

