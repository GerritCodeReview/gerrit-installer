include ../Version.mk

URL=https://storage.googleapis.com/gerrit-releases/gerrit-$(WAR_VERSION).war
CI_URL=https://gerrit-ci.gerritforge.com

NAME=gerrit
OUT=$(shell pwd)/out
BUILD_ROOT=$(shell pwd)/build

WAR=$(BUILD_ROOT)/bin/gerrit.war
PLUGINS_CI=https://gerrit-ci.gerritforge.com/job
LIBS=out-of-the-box
PLUGINS=avatars-gravatar \
  uploadvalidator

TAR_OUT=$(OUT)/gerrit-$(WAR_VERSION).tar.gz
TAR_OUT_SIG=$(TAR_OUT).asc
TAR_OUT_SHA256=$(TAR_OUT).sha256
TAR_OUT_SHA256_SIG=$(TAR_OUT_SHA256).asc
CONFIGS=$(wildcard etc/*)

all: prepare $(TAR_OUT) $(TAR_OUT_SIG) $(TAR_OUT_SHA256) $(TAR_OUT_SHA256_SIG)

clean:
	rm -Rf $(OUT)

prepare: $(CONFIGS)
	mkdir -p $(OUT)
	mkdir -p $(BUILD_ROOT)/etc
	mkdir -p $(BUILD_ROOT)/bin
	mkdir -p $(BUILD_ROOT)/plugins
	mkdir -p $(BUILD_ROOT)/lib
	mkdir -p $(BUILD_ROOT)/cache
	mkdir -p $(BUILD_ROOT)/db
	mkdir -p $(BUILD_ROOT)/git
	mkdir -p $(BUILD_ROOT)/index
	cp -R $(CONFIGS) $(BUILD_ROOT)/etc

clobber: clean
	rm -Rf $(BUILD_ROOT)

$(WAR): $(basedir $(WAR))
	curl -f -o $@  $(URL)

plugins:
	for plugin in $(PLUGINS); \
        do set -e && echo ">> Download: $$job" && \
          (curl -f -o $(BUILD_ROOT)/plugins/$$plugin.jar $(PLUGINS_CI)/plugin-$$plugin-bazel-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/$$plugin/$$plugin.jar || \
           curl -f -o $(BUILD_ROOT)/plugins/$$plugin.jar $(PLUGINS_CI)/plugin-$$plugin-bazel-master-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/$$plugin/$$plugin.jar); \
        done

libs:
	for lib in $(LIBS); \
          do set -e && echo ">> Download: $$job" && \
          (curl -f -o $(BUILD_ROOT)/lib/$$lib` $(PLUGINS_CI)/plugin-$$lib-bazel-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/$$lib/$$lib.jar || \
           curl -f -o $(BUILD_ROOT)/lib/$$lib` $(PLUGINS_CI)/plugin-$$lib-bazel-master-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/$$lib/$$lib.jar); \
        done

$(TAR_OUT): $(WAR) plugins libs $(CONFIGS)
	tar -C $(BUILD_ROOT) -f $@ -cvz .

%.asc: %
	GPG_TTY=`tty` gpg --output $@ --armor -b --sign $<

%.sha256: %
	sha256sum $< > $@

.PHONY: clean clobber prepare plugins libs
