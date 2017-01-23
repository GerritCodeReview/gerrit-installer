# Gerrit Installer For macOS

This installation does the following, it creates a user called gerrit,
it installs in /var/gerrit/.

* To build it your self do the following first, this will also create the uninstaller too under uninstaller/

```
  $ chmod a+x scripts/*
  $ chmod a+x uninstaller/scripts/*
  $ make VERSION=2.13.5
```
