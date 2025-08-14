WAR_VERSION=3.10.8
BRANCH=stable-3.10
URL=https://storage.googleapis.com/gerrit-releases/gerrit-$(WAR_VERSION).war
CI_URL=https://gerrit-ci.gerritforge.com

NAME=gerrit
OUT=$(shell pwd)/out
BUILD_ROOT=$(shell pwd)/build

WAR=$(BUILD_ROOT)/bin/gerrit.war
PLUGINS_CI=https://gerrit-ci.gerritforge.com/job
LIBS_JOBS= \
  plugin-out-of-the-box-bazel-master-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/out-of-the-box/out-of-the-box.jar
PLUGINS_JOBS= \
  plugin-avatars-gravatar-bazel-master-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/avatars-gravatar/avatars-gravatar.jar \
  plugin-uploadvalidator-bazel-$(BRANCH)/lastSuccessfulBuild/artifact/bazel-bin/plugins/uploadvalidator/uploadvalidator.jar

TAR_OUT=$(OUT)/gerrit-$(WAR_VERSION).tar.gz
CONFIGS=$(wildcard etc/*)

all: prepare $(TAR_OUT)

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
	for job in $(PLUGINS_JOBS); \
          do set -e && echo ">> Download: $$job" && curl -f -o $(BUILD_ROOT)/plugins/`basename $$job` $(PLUGINS_CI)/$$job; \
        done

libs:
	for job in $(LIBS_JOBS); \
          do set -e && echo ">> Download: $$job" && curl -f -o $(BUILD_ROOT)/lib/`basename $$job` $(PLUGINS_CI)/$$job; \
        done

$(TAR_OUT): $(WAR) plugins libs $(CONFIGS)
	tar -C $(BUILD_ROOT) -f $@ -cvz .

.PHONY: clean clobber prepare plugins libs
