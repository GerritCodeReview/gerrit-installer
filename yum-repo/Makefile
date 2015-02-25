# Customise the following variable as Make parameters
# to produce a yum.repo for a VENDOR distribution
# Default values are pointing to GerritForge (www.gerritforge.com)
VERSION=1
RELEASE=1
VENDOR=GerritForge
VENDOR_LC=$(shell echo $(VENDOR) | tr A-Z a-z)
WEB_URL=http://$(VENDOR_LC).com
MIRROR_URL=http://mirrorlist.$(VENDOR_LC).com/yum

# Vendor PGP Certificate (default GerritForge)
PGP_USER=info@$(VENDOR_LC).com
define PGP_CERT
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2.0.14 (GNU/Linux)

mQENBFTWe4gBCADSxB+UHyQ2APYVmbt40dvGsmATYgP1YmNlLfCUWkAVxkMbLqA2
WQB5t04I1uEL9bnWNS9NimA3kO5woPWygdW4fG4s7yH69mzlAMYMuCmTt6uZCiCc
eWWPtksb01rW1nxKzjVjtQWn+LNuW4sUJJSyfHNnwR/5RQV5sf6WVYSfFADtL2zZ
/wYcAl2C/SASoN55qRHGermboQjtfqMjCrCV5T1VYXaPfz+7AA01FTg6sSDrSGuJ
F+sxT/nR5rrBfB+TfgVbr+en35JOmbLaxK4xdKIauEITqaPaKNCQXhPvh0ppM1eS
8yjKBDYB36CgDZtWGeU5PrJcF/6GyyhhTsVBABEBAAG0IkdlcnJpdEZvcmdlIDxp
bmZvQGdlcnJpdGZvcmdlLmNvbT6JATgEEwECACIFAlTWe4gCGwMGCwkIBwMCBhUI
AgkKCwQWAgMBAh4BAheAAAoJEB//ql4Ycfd1aJ4IAIppWTTNI0nRUeR3poM5/8UR
nRQ4kEal0mElTpA3fuOzVylfX2c6YcdBL+y9iJsQdYNkmYeajU7661q7YZ6VL7lB
5JN9CHiMwDBdP4/dhKjIr3G4LoJZoESGh9aLJp5FedCW3JlJz/cXTLI6lyABBlDP
s4q66CyvQpsEE8meTlCACTa52tEybQt8hzv/zuS1GacIRlOsKsz4QsNiO0OkwA2C
sh12R+uTKeuje2k/L4un35bULM8tFnxaNF9AJUtTW+7+bEb1ojuYoEg6ajFkFFpY
eylZKPSRWA31wQIblWOWyiwOCaXVw9zchMFWZVk2z2zjqFdX5+8M5COIAHP/1Oi5
AQ0EVNZ7iAEIAOolcrj4zo4oOdR/YrxkBmFmbnlXY0MB2SBDQ/iXK7YITrSdp+AM
5366LbHzwsfuywoXuFCvWcNO2OAzWhyYcdFVad4J1elZ9BdXrYjcTBAsEjv/1oCA
abYLOhXl/dCzOA9lTtzRApuhsec+naZcWUGGV5lDY9aZ6T2WeeC4+GcbG7r75wDZ
CZs/rnrqgJ5kks7bhCin1wmG3CWVlxnZqijM/JMeHoYzHSdSc9uEcsqL/pGgdBX+
RiOBGziAUK14FrL7pZLFnwWK2JjirNwykMWETF9sCR8DuiLRwVPMC+iL/NmRoVsk
Kke4LJ6mmY1JE4QP1qiZusGfw0z9mUTX+PcAEQEAAYkBHwQYAQIACQUCVNZ7iAIb
DAAKCRAf/6peGHH3dZ0TB/4/dmNFVczSFrT12Qxsq4HDqscWanycC6rf7Qlzgbpu
ZTJr5Zx1NtWQmcy81mn8TCEM8bum+iTXzMfs8wW3OQ7B21NaSiuFKwgczFgXdfPe
2WeKnFz/dK+80wQZkzGf+/6Ubg/r2fsfJ5yPFB+y/uhxtINj9v12ukd0/BPGI//2
svHHVRX/ojI4TwNBw0IocOGwrznnmOqfOQ+sE0zopxRmnf1Hdh+Y6Ctrk01I8Zty
4MDduTg0uBz0PK/WGS5fxVygaee0FT3X6Q26Xp7Nx6Yyga3Rbnb5LsxTb5ImCdmY
tBf9XFXzOSNzRq91StAA9zfj3Dtxh9UfBssZsBbudNj4
=SWs9
-----END PGP PUBLIC KEY BLOCK-----
endef
export PGP_CERT

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
	-mkdir -p client etc/yum.repos.d etc/pki/rpm-gpg scripts server
	echo "$$YUM_REPO" > etc/yum.repos.d/$(VENDOR).repo
	echo "$$PGP_CERT" > etc/pki/rpm-gpg/RPM-GPG-KEY-$(VENDOR)
	echo "rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-$(VENDOR)" > scripts/after-install.sh

clean:
	-rm -Rf client etc scripts server

$(RPM_OUT): $(SRCS) prepare
	fpm -t rpm -p $@ -s dir \
	-f -n $(NAME) -v $(VERSION) --iteration $(RELEASE) --category $(CATEGORY) \
	--description "$(SUMMARY)" --url $(WEB_URL) --license "$(LICENSE)" --vendor "$(VENDOR)" \
	--depends yum \
	--after-install scripts/after-install.sh \
	--rpm-user root --rpm-group root \
	--verbose etc

server:
	echo "%_signature gpg" > ~/.rpmmacros
	echo "%_gpg_name  $(PGP_USER)" >> ~/.rpmmacros
	rpm --addsign server/*rpm
	createrepo server/.

.PHONY: clean prepare server
