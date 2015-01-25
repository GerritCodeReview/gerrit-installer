if [ -e /etc/init.d/gerrit ]
then
  GERRIT_PID=$(ps -o pid,command -u $USER | grep gerrit | awk '{print $1}')
  if [ "$GERRIT_PID" != "" ]
  then
    echo -n "Stopping Gerrit (pid=$GERRIT_PID) ..."
    /etc/init.d/gerrit stop >> /dev/null 2>> /dev/null || true
    echo "DONE" # Ignore failures as we wanted to remove it anyway
  fi
fi

