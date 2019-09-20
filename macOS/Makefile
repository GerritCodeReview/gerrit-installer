VERSION := 2.16.12

all: server

clean:
	-rm -Rf gerrit-installer.pkg
	-rm -Rf gerrit/gerrit/gerrit.war
	cd uninstaller; make clean

server:
	curl -o gerrit-$(VERSION).war https://gerrit-releases.storage.googleapis.com/gerrit-$(VERSION).war
	mv gerrit-$(VERSION).war gerrit/gerrit/gerrit.war
	pkgbuild --root ./gerrit --scripts scripts --identifier com.gerrit.gerrit --version 1 --install-location /private/var gerrit-installer.pkg
	cd uninstaller; make

.PHONY: clean server
