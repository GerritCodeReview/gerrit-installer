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
2. make install

RPM/DEBS gets created as fpm/out/gerrit-*.(deb|rpm)

### How to build other versions of Gerrit

FPM Makefile allows to customise the version and URL where Gerrit war gets downloaded.
By overriding the VERSION variable it is possible to build any Gerrit version that
is published on Google Releases Storage http://gerrit-releases.storage.googleapis.com/.

In order to build the package for Gerrit Ver. 2.9.4:

1. cd fpm
2. make VERSION=2.9.4 install

RPM/DEBS gets created as fpm/out/gerrit-2.9.4.(deb|rpm)

### How to build Gerrit 2.11/master

Gerrit 2.11/master branch is not published on Google Releases Storage, but is available
on Gerrit Build Server under the permalink: 
http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war

In order to build the package for Gerrit Ver. 2.11/master:

1. cd fpm
2. make URL=http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war VERSION=2.11

RPM/DEBS gets created as fpm/out/gerrit-2.11.(deb|rpm)

### How to create a YUM repo server

If you wish to publish the RPMs to a custom or public YUM repo server, you need
to sign the packages and create the associated yum.repo definition to be installed
on the clients.

The yum-repo directory contains a Makefile that is designed to help you in automating
the repo creation and client configuration.

In order to build a YUM repository you need to have already generated the RPMs as indicated in the previous
steps and then execute:

1. cd yum-repo
2. make 

A client RPM package will be generated under the `client` sub-directory and will need to be installed
manually on the clients in order to configure your YUM repository.

A YUM repo structure will be generated under the `server` sub-directory and will need to be uploaded to 
your HTTP Web-Server or to a public repository service (e.g. BinTray or even GitHub).

NOTE: By default the yum-repo generated will use the GerritForge credentials. Should you need to publish
      your own repository you would need to generate your own PGP private/public keys and override the
      vendor's definitions.

In order to generate a customized vendor's settings for the yum-repo, you need to execute:

1. gpg --gen-key
   [...]
   Real name: MyCompany
   Email address: info@mycompany.com
   [...]
2. gpg --export -a MyCompany > RPM-GPG-KEY-MyCompany
3. cd yum-repo
4. make VENDOR=MyCompany PGP_CERT="$(cat RPM-GPG-KEY-MyCompany)"

NOTE: The yum-repo settings are assuming that you are publishing the yum-repo server and make the URL
      listed on http://mirrorlist.mycompany.com/yum

[FPM]:https://github.com/jordansissel/fpm

