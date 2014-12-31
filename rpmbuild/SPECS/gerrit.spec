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
Requires:       java
Requires:       make
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
Gerrit is a web based code review system, facilitating online code reviews for projects using the Git version control system.

Gerrit makes reviews easier by showing changes in a side-by-side display, and allowing inline comments to be added by any reviewer.

Gerrit simplifies Git based project maintainership by permitting any authorized user to submit changes to the master Git repository, rather than requiring all approved changes to be merged in by hand by the project maintainer. This functionality enables a more centralized usage of Git.

%pre
/usr/bin/getent group gerrit || /usr/sbin/groupadd -r gerrit
/usr/bin/getent passwd gerrit || /usr/sbin/useradd -r -d $RPM_BUILD_ROOT/var/gerrit -s /sbin/nologin gerrit

%postun
/usr/sbin/userdel myservice

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/gerrit
cp -R . $RPM_BUILD_ROOT/var/gerrit/.
curl --create-dirs -o $RPM_BUILD_ROOT/var/gerrit/bin/gerrit.war  http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war
java -jar $RPM_BUILD_ROOT/var/gerrit/bin/gerrit.war init --batch -d $RPM_BUILD_ROOT/var/gerrit

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,gerrit,gerrit,-)
%doc
/var/gerrit



%changelog
