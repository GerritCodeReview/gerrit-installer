GERRIT_SITE=/var/gerrit
grep -q gerrit /etc/passwd || echo -n "Creating Gerrit user ... " && useradd gerrit -d $GERRIT_SITE --create-home && echo "DONE"

echo -n "Checking Java version ... "
JAVA_VERSION=$(java -version 2>&1)
[ $? != 0 ] && echo -e "NOT FOUND\nPlease install Java >= 1.7.0 and try again" && exit 1

VERSION=`expr "$JAVA_VERSION" : '.*"\(1.[0-9\.]*\)["_]'`
echo "$VERSION"
test "$VERSION" "<" "1.7" && echo "ERROR: java >= 1.7.0 required by Gerrit" || true
test "$VERSION" ">" "1.7"
