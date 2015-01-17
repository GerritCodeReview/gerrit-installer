Gerrit Native Installation Packages
===================================
This project contains the native Gerrit installation packages for the most
popular platforms:

- Linux (RPM and Debian packages)
- MacOSX (DMG)
- Windows (MSI)

Linux RPM/DEB
-------------
fpm subdirectory contains the Makefile to create RPM and DEB packages for
a basic Gerrit installation with the following options:

- site: /var/gerrit
- user: gerrit
- auth: development`_`become`_`any`_`account

### How to build

You need to have a Linux with the [FPM] utility installed.
Then execute the following steps from the cloned gerrit-installer project workspace:

1. cd fpm
2. make

RPM/DEBS gets created as fpm/out/gerrit-*.(deb|rpm)

### How to build other versions of Gerrit

FPM Makefile allows to customise the version and URL where Gerrit war gets downloaded.
By overriding the VERSION variable it is possible to build any Gerrit version that
is published on Google Releases Storage http://gerrit-releases.storage.googleapis.com/.

In order to build the package for Gerrit Ver. 2.9.4:

1. cd fpm
2. make VERSION=2.9.4

RPM/DEBS gets created as fpm/out/gerrit-2.9.4.(deb|rpm)

### How to build Gerrit 2.11/master

Gerrit 2.11/master branch is not published on Google Releases Storage, but is available
on Gerrit Build Server under the permalink: http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war

In order to build the package for Gerrit Ver. 2.11/master:

1. cd fpm
2. make URL=http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war VERSION=2.11

RPM/DEBS gets created as fpm/out/gerrit-2.11.(deb|rpm)

[FPM]:https://github.com/jordansissel/fpm

