SUDO="sudo -u $USER"
LOG=/tmp/gerrit-installer.log

echo ""
echo -n "Initialising Gerrit site ... "
$SUDO java -jar $GERRIT_SITE/bin/gerrit.war init --batch -d $GERRIT_SITE >>$LOG 2>>$LOG
[ $? != 0 ] && echo "FAILED" && exit 1
echo "DONE"

echo -n "Reindexing Gerrit ... "
$SUDO java -jar $GERRIT_SITE/bin/gerrit.war reindex -d $GERRIT_SITE >> $LOG 2>>$LOG
[ $? != 0 ] && echo "FAILED" && exit 2
echo "DONE"

echo -n "Setting user/group ownership ..."
chown -R $USER:$GROUP $GERRIT_SITE

echo -n "Creating symlinks ... "
cd /etc/init.d && ln -sf $GERRIT_SITE/bin/gerrit.sh gerrit
cd /var/log && ln -sf $GERRIT_SITE/logs gerrit
cd /etc && ln -sf $GERRIT_SITE/etc gerrit
[ ! -d /etc/default ] && mkdir -p /etc/default
cd /etc/default && ln -sf /etc/gerrit/gerritcodereview
echo "DONE"

echo ""
echo "Installation completed"
echo ""
echo "To start Gerrit server, run: /etc/init.d/gerrit start"
echo "To start using Gerrit, open: http://$(hostname):8080/"
