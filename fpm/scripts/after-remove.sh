GERRIT_SITE=/var/gerrit
rm -f /etc/init.d/gerrit || true
rm -f /var/log/gerrit || true
rm -f /etc/gerrit || true
rm /etc/default/gerritcodereview || true
userdel gerrit || true
