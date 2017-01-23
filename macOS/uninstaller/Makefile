all: server

clean:
	-rm -Rf gerrit-uninstaller.pkg

server:
	pkgbuild --root ../gerrit --scripts scripts --identifier com.gerrit.gerrit --version 1 --install-location /private/var/gerr-temp gerrit-uninstaller.pkg

.PHONY: clean server
