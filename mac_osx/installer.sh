#!/bin/sh

wget https://gerrit-releases.storage.googleapis.com/gerrit-2.13.5.war

mv gerrit-2.13.5.war gerrit2/gerrit2/gerrit.new

pkgbuild --root ./gerrit2 --scripts scripts --identifier com.gerrit.gerrit --version 1 --install-location /private/var/lib gerrit-installer.pkg
