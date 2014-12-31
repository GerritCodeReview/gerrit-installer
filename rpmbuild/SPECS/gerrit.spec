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
BuildRequires:  rpm >= 4.4
Requires:       git
Requires:       rpm >= 4.4
Requires(pretrans): /usr/sbin/useradd, /usr/bin/grep, /usr/bin/test
Requires(post): /usr/bin/sudo, /usr/bin/ln, /usr/sbin/chkconfig, /usr/sbin/service, /usr/bin/mkdir, /usr/bin/chown
Requires(postun): /usr/sbin/userdel, /usr/bin/rm

%description
Gerrit is a web based code review system, facilitating online code reviews for projects using the Git version control system.

Gerrit makes reviews easier by showing changes in a side-by-side display, and allowing inline comments to be added by any reviewer.

Gerrit simplifies Git based project maintainership by permitting any authorized user to submit changes to the master Git repository, rather than requiring all approved changes to be merged in by hand by the project maintainer. This functionality enables a more centralized usage of Git.

%pretrans
echo -n "Creating Gerrit user ... "
/usr/bin/grep -q gerrit /etc/passwd || /usr/sbin/useradd gerrit
echo -n "Checking Java version ... "
JAVA_VERSION=$(java -version 2>&1)
VERSION=`expr "$JAVA_VERSION" : '.*"\(1.[0-9\.]*\)["_]'`
echo "$VERSION"
test "$VERSION" "<" "1.7" && echo "ERROR: java >= 1.7.0 required by Gerrit" || true
test "$VERSION" ">" "1.7"

%post
GERRIT_SITE=/var/gerrit
/usr/bin/sudo -u gerrit java -jar /var/gerrit/bin/gerrit.war init --batch -d $GERRIT_SITE
/usr/bin/sudo -u gerrit java -jar /var/gerrit/bin/gerrit.war reindex -d $GERRIT_SITE
/usr/bin/ln -sf $GERRIT_SITE/bin/gerrit.sh /etc/init.d/gerrit
/usr/bin/ln -sf $GERRIT_SITE/logs /var/log/gerrit
/usr/bin/ln -sf $GERRIT_SITE/etc /etc/gerrit
/usr/sbin/chkconfig --add /etc/init.d/gerrit

%preun
/var/gerrit/bin/gerrit.sh stop

%postun
/usr/sbin/userdel -r gerrit
/usr/sbin/chkconfig --del /etc/init.d/gerrit
/usr/bin/rm /etc/init.d/gerrit
/usr/bin/rm /var/log/gerrit
/usr/bin/rm /etc/gerrit

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/gerrit/etc
mkdir -p $RPM_BUILD_ROOT/etc/default
cp gerrit.config $RPM_BUILD_ROOT/var/gerrit/etc/.
cp gerritcodereview $RPM_BUILD_ROOT/etc/default/gerritcodereview
curl --create-dirs -o $RPM_BUILD_ROOT/var/gerrit/bin/gerrit.war  http://ci.gerritforge.com/job/Gerrit-master/lastSuccessfulBuild/artifact/buck-out/gen/gerrit.war

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,gerrit,gerrit,-)
/var/gerrit
/var/gerrit/bin/gerrit.war
%config /etc/default/gerritcodereview 
%config /var/gerrit/etc/gerrit.config

%doc

%changelog
