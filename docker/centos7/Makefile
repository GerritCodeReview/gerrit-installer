# Customise the following variable as Make parameters
# to produce a yum.repo for a VENDOR distribution
# Default values are pointing to GerritForge (www.gerritforge.com)
VERSION=2.16.17
RELEASE=1
REPO_VERSION=1
REPO_RELEASE=1
VENDOR=GerritForge
VENDOR_LC=$(shell echo $(VENDOR) | tr A-Z a-z)
IMAGE=$(VENDOR_LC)/gerrit-centos7
NO_CACHE=true

# End of the variables that can be customized

define DOCKERFILE
FROM centos:7.5.1804
MAINTAINER $(VENDOR)

# Allow remote connectivity and sudo
RUN yum -y install openssh-client initscripts sudo

# Add Gerrit packages repository
RUN rpm -i https://$(VENDOR_LC).com/$(VENDOR_LC)-repo-$(REPO_VERSION)-$(REPO_RELEASE).noarch.rpm

# Install OpenJDK and Gerrit in two subsequent transactions
# (pre-trans Gerrit script needs to have access to the Java command)
RUN yum -y install java-1.8.0-openjdk
RUN yum -y install gerrit-$(VERSION)-$(RELEASE)

USER gerrit
RUN java -jar /var/gerrit/bin/gerrit.war init --batch --install-all-plugins -d /var/gerrit
RUN java -jar /var/gerrit/bin/gerrit.war reindex -d /var/gerrit

# Allow incoming traffic
EXPOSE 29418 8080

VOLUME ["/var/gerrit/git", "/var/gerrit/index", "/var/gerrit/cache", "/var/gerrit/db", "/var/gerrit/etc"]

# Start Gerrit
CMD /var/gerrit/bin/gerrit.sh start && tail -f /var/gerrit/logs/error_log
endef
export DOCKERFILE

image: prepare
	echo "$$DOCKERFILE" > Dockerfile
	docker build --no-cache=$(NO_CACHE) -t $(IMAGE):$(VERSION) .

clean:
	-rm Dockerfile

prepare:
	echo "$$DOCKERFILE" > Dockerfile

run: image
	docker run -d --hostname $$HOSTNAME -p 8080:8080 -p 29418:29418 $(IMAGE):$(VERSION)

.PHONY: clean prepare image
