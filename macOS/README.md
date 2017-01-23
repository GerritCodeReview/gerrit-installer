# Gerrit Installer For macOS

This installation does the following, it creates a user called gerrit,
it installs in /var/gerrit/.

* To build it your self do the following first

```
  $ chmod a+x scripts/*
  $ chmod a+x uninstaller/scripts/*
  $ ./installer.sh
  $ make VERSION=2.13.5
```

To create the uninstaller run the following script from bash (Note: You may need to do sudo ./uninstaller.sh)

```
  $ cd uninstaller
  $ make
```
