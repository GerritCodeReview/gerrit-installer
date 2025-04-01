# Customise the following variable as Make parameters
# to produce a yum.repo for a VENDOR distribution
# Default values are pointing to GerritForge (www.gerritforge.com)
VERSION=1
RELEASE=1
VENDOR=GerritForge
VENDOR_LC=$(shell echo $(VENDOR) | tr A-Z a-z)
WEB_URL=http://$(VENDOR_LC).com
MIRROR_URL=http://mirrorlist.$(VENDOR_LC).com/deb

# Vendor PGP Key ID (default GerritForge)
PGP_KEY_ID=72ADB205736D7147DA56E8C955787ED781304950
### END OF VARIABLES THAT CAN BE OVERRIDDEN ###

define DEB_RELEASE
Origin: $(VENDOR)
Suite: gerrit
Label: gerrit
Codename: gerrit
Description: Gerrit Code Review distribution
Version: $(VERSION)
endef
export DEB_RELEASE

DEB_REPO="deb mirror://mirrorlist.$(VENDOR_LC).com/deb gerrit contrib"

CATEGORY=Development
SUMMARY=$(VENDOR) repository
BUILD_ARCH=noarch
LICENSE=Apache 2.0
NAME=$(VENDOR_LC)-repo

all: server

prepare:
	-mkdir -p etc/apt/sources.list.d scripts server
	echo "$$DEB_REPO" > etc/apt/sources.list.d/$(VENDOR).list
	echo "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $(PGP_KEY_ID)" > scripts/after-install.sh

clean:
	-rm -Rf etc scripts server

server:
	debsigs --sign=origin -k $(PGP_KEY_ID) server/dists/gerrit/contrib/binary-i386/*.deb
	-mkdir -p server/dists/gerrit/contrib/binary-amd64
	-mkdir -p server/dists/gerrit/contrib/binary-arm64
	cp -f server/dists/gerrit/contrib/binary-i386/*.deb server/dists/gerrit/contrib/binary-amd64
	cp -f server/dists/gerrit/contrib/binary-i386/*.deb server/dists/gerrit/contrib/binary-arm64
	echo "$$DEB_RELEASE" >> server/Release
	cd server && apt-ftparchive packages dists/gerrit/contrib/binary-i386 > dists/gerrit/contrib/binary-i386/Packages
	cd server && apt-ftparchive packages dists/gerrit/contrib/binary-amd64 > dists/gerrit/contrib/binary-amd64/Packages
	cd server && apt-ftparchive packages dists/gerrit/contrib/binary-arm64 > dists/gerrit/contrib/binary-arm64/Packages
	cd server && apt-ftparchive release dists/gerrit >> Release
	gpg -abs --default-key $(PGP_KEY_ID) -o server/Release.gpg server/Release
	mv server/Release* server/dists/gerrit/.

.PHONY: clean prepare server
