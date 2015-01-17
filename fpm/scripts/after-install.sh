GERRIT_SITE=/var/gerrit
SUDO="sudo -u gerrit"
$SUDO java -jar /var/gerrit/bin/gerrit.war init --batch -d $GERRIT_SITE
$SUDO java -jar /var/gerrit/bin/gerrit.war reindex -d $GERRIT_SITE
cd /etc/init.d && ln -sf $GERRIT_SITE/bin/gerrit.sh gerrit
cd /var/log && ln -sf $GERRIT_SITE/logs gerrit
cd /etc && ln -sf $GERRIT_SITE/etc gerrit
[ ! -d /etc/default ] && mkdir -p /etc/default
cd /etc/default && ln -sf /etc/gerrit/gerritcodereview
