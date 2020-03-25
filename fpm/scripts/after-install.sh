SUDO="sudo -u $USER"
LOG=/tmp/gerrit-installer.log
chmod a+rw $LOG

[ -d /etc/default ] || mkdir -p /etc/default
[ -f /etc/default/gerritcodereview ] || echo "GERRIT_SITE=$GERRIT_SITE" > /etc/default/gerritcodereview

echo ""
echo -n "Initialising Gerrit site ... "
$SUDO java -jar $GERRIT_SITE/bin/gerrit.war init --batch --install-all-plugins -d $GERRIT_SITE >>$LOG 2>>$LOG
[ $? != 0 ] && echo "FAILED" && exit 1
echo "DONE"

echo -n "Setting user/group owner ... "
chown -R $USER:$GROUP $GERRIT_SITE
echo "DONE"

echo -n "Creating symlinks .......... "
cd /etc/init.d && ln -sf $GERRIT_SITE/bin/gerrit.sh gerrit
cd /var/log && ln -sf $GERRIT_SITE/logs gerrit
cd /etc && ln -sf $GERRIT_SITE/etc gerrit
echo "DONE"

echo ""
echo "Installation completed"
echo ""

URL=$(git config -f /etc/gerrit/gerrit.config gerrit.canonicalWebUrl)
[ -z "$URL" ] || echo "To start using Gerrit, run '/etc/init.d/gerrit start' and open: $URL"
