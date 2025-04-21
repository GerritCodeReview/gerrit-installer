# Customise the following variable as Make parameters
# to produce a yum.repo for a VENDOR distribution
# Default values are pointing to GerritForge (www.gerritforge.com)
VERSION=1
RELEASE=5
VENDOR=GerritForge
VENDOR_LC=$(shell echo $(VENDOR) | tr A-Z a-z)
VENDOR_USER=gerrit
WEB_URL=http://$(VENDOR_LC).com
MIRROR_URL=http://mirrorlist.$(VENDOR_LC).com/yum

# Vendor PGP Certificate (default GerritForge)
PGP_USER=$(VENDOR_USER)@$(VENDOR_LC).com

### END OF VARIABLES THAT CAN BE OVERRIDDEN ###

# Yum repo definition
define YUM_REPO
[$(VENDOR_LC)]
name=$(VENDOR) repository for Gerrit Code Review
mirrorlist=$(MIRROR_URL)
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-$(VENDOR)
endef
export YUM_REPO

CATEGORY=Development
SUMMARY=$(VENDOR) repository
BUILD_ARCH=noarch
LICENSE=Apache 2.0
NAME=$(VENDOR_LC)-repo
RPM_OUT=client/$(VENDOR_LC)-repo-$(VERSION)-$(RELEASE).$(BUILD_ARCH).rpm

all: client server

client: $(RPM_OUT)

prepare:
	-mkdir -p client etc/yum.repos.d etc/pki/rpm-gpg server
	echo "$$YUM_REPO" > etc/yum.repos.d/$(VENDOR).repo
	gpg --yes --armor --output etc/pki/rpm-gpg/RPM-GPG-KEY-$(VENDOR) --export $(PGP_USER)

clean:
	-rm -Rf client etc server

$(RPM_OUT): $(SRCS) prepare
	fpm -t rpm -p $@ -s dir \
	-f -n $(NAME) -v $(VERSION) --iteration $(RELEASE) --category $(CATEGORY) -a all --rpm-os linux \
	--description "$(SUMMARY)" --url $(WEB_URL) --license "$(LICENSE)" --vendor "$(VENDOR)" \
	--rpm-user root --rpm-group root \
	--verbose etc

server:
	echo "%_signature gpg" > ~/.rpmmacros
	echo "%_gpg_name  $(PGP_USER)" >> ~/.rpmmacros
	echo '%__gpg_sign_cmd %{__gpg} \
 gpg --force-v3-sigs --digest-algo=sha256 --batch --no-verbose --no-armor \
 --passphrase-fd 3 --no-secmem-warning -u "%{_gpg_name}" \
 -sbo %{__signature_filename} %{__plaintext_filename}' >>  ~/.rpmmacros
	rpm --addsign server/*rpm
	createrepo --checksum sha server/.

.PHONY: clean prepare server
