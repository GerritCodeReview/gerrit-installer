Name:           gerrit
Version:        2.11
Release:        1
Summary:        Gerrit Code Review
BuildArch:      noarch

Group:          Development
License:        Apache 2.0
URL:            https://code.google.com/p/gerrit/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  curl
BuildRequires:  make
Requires:       git
Requires:       make
Requires:       rpm >= 4.4
Requires: 	coreutils
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
Gerrit is a web based code review system, facilitating online code reviews for projects using the Git version control system.

Gerrit makes reviews easier by showing changes in a side-by-side display, and allowing inline comments to be added by any reviewer.

Gerrit simplifies Git based project maintainership by permitting any authorized user to submit changes to the master Git repository, rather than requiring all approved changes to be merged in by hand by the project maintainer. This functionality enables a more centralized usage of Git.

%pretrans
echo -n "Checking Java version ... "
JAVA_VERSION=$(java -version 2>&1)
VERSION=`expr "$JAVA_VERSION" : '.*"\(1.[0-9\.]*\)["_]'`
echo "$VERSION"
test "$VERSION" "<" "1.7" && echo "ERROR: java >= 1.7.0 required by Gerrit" || true
test "$VERSION" ">" "1.7"

%pre
/usr/bin/getent group gerrit || /usr/sbin/groupadd -r gerrit
/usr/bin/getent passwd gerrit || /usr/sbin/useradd -r -d $RPM_BUILD_ROOT/var/gerrit gerrit

%post
sudo -u gerrit java -jar /var/gerrit/bin/gerrit.war init --batch -d /var/gerrit

%prep

%build
echo "building"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/gerrit
cp -R . $RPM_BUILD_ROOT/var/gerrit/.
curl --create-dirs -o $RPM_BUILD_ROOT/var/gerrit/bin/gerrit.war  http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,gerrit,gerrit,-)
%doc
/var/gerrit



%changelog
