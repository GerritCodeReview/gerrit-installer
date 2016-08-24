VERSION=2.12.4
URL=http://gerrit-releases.storage.googleapis.com/gerrit-$(VERSION).war
RELEASE=1

NAME=gerrit
CATEGORY=Development
SUMMARY=Gerrit Code Review
BUILD_ARCH=noarch
BUILD_ROOT=build/root
SCRIPTS_ROOT=build/scripts
OUT=out
USER=gerrit
GROUP=gerrit
GERRIT_SITE=/var/gerrit

LICENSE=Apache 2.0
VENDOR=
WEB_URL=https://code.google.com/p/gerrit/

WAR=$(BUILD_ROOT)/bin/gerrit.war

RPM_OUT=$(OUT)/gerrit-$(VERSION)-$(RELEASE).$(BUILD_ARCH).rpm
DEB_OUT=$(OUT)/gerrit-$(VERSION)-$(RELEASE).$(BUILD_ARCH).deb
YUM_INSTALL=../yum-repo/server
DEB_INSTALL=../deb-repo/server/dists/gerrit/contrib/binary-i386
CONFIGS=$(wildcard etc/*)
SCRIPTS=$(foreach script,$(wildcard scripts/*),$(notdir $(script)))
BUILD_SCRIPTS=$(foreach script,$(SCRIPTS),$(SCRIPTS_ROOT)/$(script))

FPM_OPTS=-s dir \
	-f -n $(NAME) -v $(VERSION) --iteration $(RELEASE) --category $(CATEGORY) -a $(BUILD_ARCH) \
	--description "$(SUMMARY)" --url $(WEB_URL) --license "$(LICENSE)" --vendor "$(VENDOR)" \
	--depends git \
	--PKG-user $(USER) --PKG-group $(GROUP) \
	--before-install $(SCRIPTS_ROOT)/before-install.sh \
	--after-install $(SCRIPTS_ROOT)/after-install.sh \
	--before-remove $(SCRIPTS_ROOT)/before-remove.sh \
	--after-remove $(SCRIPTS_ROOT)/after-remove.sh \
	--prefix $(GERRIT_SITE) --directories $(GERRIT_SITE) --config-files $(GERRIT_SITE)/etc \
	--verbose -C $(BUILD_ROOT) .

RPM_OPTS=$(subst --before-install,--rpm-pretrans, $(subst PKG,rpm,$(FPM_OPTS)))
DEB_OPTS=$(subst PKG,deb,$(FPM_OPTS))

all: prepare $(RPM_OUT) $(DEB_OUT)

rpm: $(RPM_OUT)

deb: $(DEB_OUT)

clean:
	rm -Rf $(OUT)

prepare: $(CONFIGS)
	mkdir -p $(OUT)
	mkdir -p $(SCRIPTS_ROOT)
	mkdir -p $(BUILD_ROOT)/etc
	mkdir -p $(BUILD_ROOT)/bin
	cp $(CONFIGS) $(BUILD_ROOT)/etc
	-groupadd $(GROUP)
	$(eval GROUP_ID := $(shell /usr/bin/getent group $(GROUP) | cut -d ':' -f 3))
	-useradd -g $(GROUP_ID) $(USER)

install-rpm: $(RPM_OUT)
	-mkdir -p $(YUM_INSTALL)
	cp $(RPM_OUT) $(YUM_INSTALL)

install-deb: $(DEB_OUT)
	-mkdir -p $(DEB_INSTALL)
	cp $(DEB_OUT) $(DEB_INSTALL)

install: install-rpm install-deb

clobber: clean
	rm -Rf $(BUILD_ROOT)
	rm -Rf $(SCRIPTS_ROOT)

$(WAR): $(basedir $(WAR))
	curl -o $@  $(URL)

$(SCRIPTS_ROOT)/%.sh: scripts/%.sh
	echo "#!/bin/bash" > $@
	echo "USER=$(USER)" >> $@
	echo "GROUP=$(GROUP)" >> $@
	echo "GERRIT_SITE=$(GERRIT_SITE)" >> $@
	cat $< >> $@

$(RPM_OUT): $(WAR) $(CONFIGS) $(BUILD_SCRIPTS) chown
	fpm -t rpm -p $@ $(RPM_OPTS)

$(DEB_OUT): $(WAR) $(CONFIGS) $(BUILD_SCRIPTS) chown
	fpm -t deb -p $@ $(DEB_OPTS)

.PHONY: clean clobber prepare chown rpm deb install install-deb install-rpm
