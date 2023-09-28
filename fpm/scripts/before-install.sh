LOG=/tmp/gerrit-installer.log
[ ! -f $LOG ] || chmod a+rw $LOG
echo "Using log file $LOG"

GROUP_ID=$(/usr/bin/getent group $GROUP | cut -d ':' -f 3 2>> $LOG || true)
if [ "$GROUP_ID" == "" ]
then
  echo -n "Creating $GROUP group ... "
  groupadd $GROUP >> $LOG 2>> $LOG
  [ $? != 0 ] && echo "FAILED" && exit 1
  GROUP_ID=$(/usr/bin/getent group $GROUP | cut -d ':' -f 3 2>> $LOG || true)
  echo "DONE"
fi

USER_PASSWD=$(/usr/bin/getent passwd $USER 2>> $LOG || true)
if [ "$USER_PASSWD" == "" ]
then
  echo -n "Creating $USER user ... "
  useradd $USER -M -g $GROUP_ID -d $GERRIT_SITE >> $LOG 2>> $LOG
  [ $? != 0 ] && echo "FAILED" && exit 1
  echo "DONE"
fi


echo -n "Checking Java version ... "
JAVA_VERSION=$(java -version 2>&1)
[ $? != 0 ] && echo -e "NOT FOUND\nPlease install Java 11 and try again" && exit 2

VERSION=`expr "$JAVA_VERSION" : '.*"\(1[17]\..*\)["_]'`
echo "$VERSION"
test "$VERSION" "<" "11" && echo "ERROR: Java 11 or 17 required by Gerrit" && exit 3

# Script is invoked even before upgrade, we need to stop Gerrit if active
GERRIT_PID=$(ps -o pid,command -u $USER | grep gerrit | awk '{print $1}')
if [ "$GERRIT_PID" != "" ]
then
  echo -n "Stopping Gerrit (pid=$GERRIT_PID) ... "
  if [ -e /etc/init.d/gerrit ]
  then
    /etc/init.d/gerrit stop >> $LOG 2>> $LOG
    [ $? != 0 ] && echo "FAILED" && exit 1
    echo "DONE"
  else
    echo "Cannot locate init.d script for Gerrit" | tee -a $LOG
    echo "Please stop Gerrit (pid=$GERRIT_PID) manually and try the installation again" | tee -a $LOG
    echo "FAILED" && exit 1
  fi
fi

exit 0
