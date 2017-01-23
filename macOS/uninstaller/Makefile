all: uninstall

clean:
	-rm -Rf gerrit-uninstaller.pkg

uninstall:
	pkgbuild --root ./gerr-temp --scripts scripts --identifier com.gerrit.gerrit --version 1 --install-location /private/var/gerr-temp gerrit-uninstaller.pkg

.PHONY: clean uninstall
