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
PGP_KEY_ID=1871F775
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
DEB_OUT=client/$(VENDOR_LC)-repo-$(VERSION)-$(RELEASE).$(BUILD_ARCH).deb

all: client server

client: $(RPM_OUT) 

prepare:
	-mkdir -p client etc/apt/sources.list.d scripts server
	echo "$$DEB_REPO" > etc/apt/sources.list.d/$(VENDOR).repo
	echo "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $(PGP_KEY_ID)" > scripts/after-install.sh

clean:
	-rm -Rf client etc scripts server

$(RPM_OUT): $(SRCS) prepare
	fpm -t deb -p $@ -s dir \
	-f -n $(NAME) -v $(VERSION) --iteration $(RELEASE) --category $(CATEGORY) \
	--description "$(SUMMARY)" --url $(WEB_URL) --license "$(LICENSE)" --vendor "$(VENDOR)" \
	--depends apt \
	--after-install scripts/after-install.sh \
	--deb-user root --deb-group root \
	--verbose etc

server:
	debsigs --sign=origin -k $(PGP_KEY_ID) server/dists/gerrit/contrib/binary-i386/*.deb
	echo "$$DEB_RELEASE" >> server/Release
	cd server && apt-ftparchive packages dists/gerrit/contrib/binary-i386 > dists/gerrit/contrib/binary-i386/Packages
	bzip2 -f server/dists/gerrit/contrib/binary-i386/Packages
	cd server && apt-ftparchive release dists/gerrit >> Release
	gpg -abs -o server/Release.gpg server/Release
	mv server/Release* server/dists/gerrit/.

.PHONY: clean prepare server
