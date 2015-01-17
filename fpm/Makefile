VERSION=2.10-rc1
URL=http://gerrit-releases.storage.googleapis.com/gerrit-$(VERSION).war
RELEASE=1

NAME=gerrit
CATEGORY=Development
SUMMARY=Gerrit Code Review
BUILD_ARCH=noarch
BUILD_ROOT=build
OUT=out
ETC=etc
USER=gerrit
GROUP=gerrit
GERRIT_SITE=/var/gerrit

License=Apache 2.0
WEB_URL=https://code.google.com/p/gerrit/

WAR=$(BUILD_ROOT)/bin/gerrit.war

RPM_OUT=$(OUT)/gerrit-$(VERSION)-$(RELEASE).$(BUILD_ARCH).rpm
DEB_OUT=$(OUT)/gerrit-$(VERSION)-$(RELEASE).$(BUILD_ARCH).deb
CONFIGS=$(wildcard $(ETC)/*)

FPM_OPTS=-s dir \
	-n $(NAME) -v $(VERSION) --iteration $(RELEASE) --category $(CATEGORY) \
	--description "$(SUMMARY)" --url $(WEB_URL) \
	--depends git \
	--PKG-user $(USER) --PKG-group $(GROUP) \
	--before-install scripts/before-install.sh \
	--after-install scripts/after-install.sh \
	--before-remove scripts/before-remove.sh \
	--after-remove scripts/after-remove.sh \
	--prefix $(GERRIT_SITE) --directories $(GERRIT_SITE) --config-files $(GERRIT_SITE)/etc \
	--verbose -C $(BUILD_ROOT) .

RPM_OPTS=$(subst PKG,rpm,$(FPM_OPTS))
DEB_OPTS=$(subst PKG,deb,$(FPM_OPTS))

all: prepare $(RPM_OUT) $(DEB_OUT)

clean:
	rm -Rf $(OUT)
	-grep -q gerrit /etc/passwd && userdel gerrit 

prepare:
	-grep -v -q gerrit /etc/passwd && useradd gerrit
	mkdir -p $(OUT)
	mkdir -p $(BUILD_ROOT)/etc/.
	cp $(CONFIGS) $(BUILD_ROOT)/etc/.

clobber: clean
	rm -Rf $(BUILD_ROOT)

$(WAR): 
	curl --create-dirs -o $@  $(URL)
	
chown:
	chown -R $(USER): $(BUILD_ROOT)

$(RPM_OUT): $(WAR) $(CONFIGS) chown
	fpm -t rpm -p $@ $(RPM_OPTS) 

$(DEB_OUT): $(WAR) $(CONFIGS) chown
	fpm -t deb -p $@ $(DEB_OPTS)

.PHONY: clean clobber prepare chown
