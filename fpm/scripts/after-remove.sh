if [ "$1" != "1" ] # Don't execute during upgrade
then
  rm -f /etc/init.d/gerrit || true
  rm -f /var/log/gerrit || true
  rm -f /etc/gerrit || true
  rm /etc/default/gerritcodereview || true
fi
