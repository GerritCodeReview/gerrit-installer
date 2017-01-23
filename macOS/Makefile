VERSION=2.13.5

all: server

prepare:
	wget https://gerrit-releases.storage.googleapis.com/gerrit-$(VERSION).war
	mv gerrit-$(VERSION).war gerrit/gerrit/gerrit.war

clean:
	-rm -Rf gerrit-installer.pkg
        -rm -RF gerrit/gerrit/gerrit.war

server:
	pkgbuild --root ./gerrit --scripts scripts --identifier com.gerrit.gerrit --version 1 --install-location /private/var gerrit-installer.pkg

.PHONY: clean prepare server
